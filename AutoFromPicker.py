# AutoFromPicker plugin for Mail.app
# (C) Copyright 2012 Matthew Somerville
# Copyright 2003-2011, James R. Eagan (code at my last name dot me)
# Nagging and whining and intermittent Maintaining by Stefan Magdalinski
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# and GNU Lesser General Public License along with this program.  
# If not, see <http://www.gnu.org/licenses/>.
# Set up

from AppKit import *
from Foundation import *
import objc
import PyObjCTools.AppHelper

from config import *

ModuleBundle = objc.currentBundle()    
MVMailBundle = objc.lookUpClass('MVMailBundle')
MailDocumentEditor = objc.lookUpClass('MailDocumentEditor')
HeadersEditor = objc.lookUpClass('HeadersEditor')

# Register this module
class AutoFromPicker(MVMailBundle):
    @classmethod
    def initialize(cls):
        cls.registerBundle()
        NSLog(u"AutoFromPicker plugin registered with Mail")

# This is a helper function that swaps an internal Mail function with a
# function in this file. Called as a decorator on the new function you want to
# use instead, which will be passed the original function as its first argument
def swizzle(*args):
    cls, SEL = args
    def decorator(func):
        oldIMP      = cls.instanceMethodForSelector_(SEL)
        def wrapper(self, *args, **kwargs):
            return func(self, oldIMP, *args, **kwargs)
        newMethod   = objc.selector(wrapper, selector = oldIMP.selector, signature = oldIMP.signature)
        objc.classAddMethod(cls, SEL, newMethod)
        return wrapper
    return decorator

# This sets the sender for the message to the address provided. It should also
# update the visible look, but this doesn't always work in Lion.
def updateSenderAndNotify(backend, to):
    backend.setSender_(to)
    # Below does not exist any more :( And don't know what argument to pass to _mailAccountDidChange_
    try:
        backend.delegate().headersEditor().mailAccountsDidChange()
    except:
        pass

class MailDocumentEditor(objc.Category(MailDocumentEditor)):
    # Main checking function, called in the three cases. Checks To against provided data,
    # and alerts or changes account.
    def checkRecipients(self, alert=False):
        backend = self.backEnd()
        try:
            from_line = backend.message().mutableHeaders().addressListForKey_(u"from")[0]
        except:
            from_line = backend.message().mutableHeaders().headersForKey_(u"from")
        to_line = backend.allRecipients()
        if to_line:
            for to in to_line:
                NSLog('%s %s' % (from_line, to))
                for account, strings in ACCOUNTS.items():
                    for string in strings:
                         if string.lower() in to.lower() and from_line.lower() != account.lower():
                            if alert:
                                self.fromAlertSheet()
                                return False
                            else:
                                NSLog('[AFP] switching account to %s' % account)
                                updateSenderAndNotify(backend, account)
                                return True
        return True

    # Function that displays a modal dialogue box
    def fromAlertSheet(self):
        alert = NSAlert.alloc().init()
        alert.addButtonWithTitle_('Send')
        alert.addButtonWithTitle_('Cancel')
        alert.setMessageText_('Message Has Incorrect From')
        alert.setInformativeText_("Your mail is to work addresses, but is not from your work address. Do you wish to continue?")
        alert.beginSheetModalForWindow_modalDelegate_didEndSelector_contextInfo_( self.window(), self, self.fromAlertSheetDidEnd, 0)

    # What to do when one of the dialogue box buttons are clicked
    def fromAlertSheetDidEnd(self, panel, returnCode, contextInfo):
        if returnCode == NSAlertFirstButtonReturn:
            self.send_(contextInfo)
        else:
            NSLog('User cancelled sending message.')
    fromAlertSheetDidEnd = PyObjCTools.AppHelper.endSheetMethod(fromAlertSheetDidEnd)

# If desired, replace the function that runs when you hit Reply with one that
# checks the To: list and then calls the original function
if SET_ON_REPLY:
    @swizzle(MailDocumentEditor, 'finishLoadingEditor')
    def finishLoadingEditor(self, original):
        NSLog('[AFP] finishLoadingEditor')
        self.checkRecipients()
        original(self)

# If desired, replace the function that runs when you change the recipients to one that
# calls the original function, then checks the To: list to possibly update sender
if SET_ON_RECIPIENT_UPDATE:
    @swizzle(HeadersEditor, 'recipientsDidChange:')
    def recipientsDidChange(self, original, sender):
        NSLog('[AFP] recipientsDidChange')
        original(self, sender)
        try:
            objc.getInstanceVariable(self, '_documentEditor').checkRecipients()
        except:
            objc.getInstanceVariable(self, 'documentEditor').checkRecipients()

# If desired, replace the function called when you hit Send with one that
# checks the recipients, possibly shows a dialogue box, or otherwise just
# sends.
if ALERT_ON_SEND:
    @swizzle(MailDocumentEditor, 'send:')
    def send(self, original, sender):
        NSLog('[AFP] send:')
        if self.checkRecipients(True):
            original(self, sender)

