# AutoFromPicker plugin for Mail.app
# (C) Copyright 2012 Matthew Somerville
# Based on Attachment Scanner Plugin by James R. Eagan (code at my last name dot me)
# Nagging and whining and unreliable maintaining by Stefan Magdalinski (stefan at whitelabel.org)
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
# Config file

# When you hit reply, should it change the account
SET_ON_REPLY = True

# When you change To/CC/etc when writing a reply, should it change the account (no visible notification in Lion BUG)
SET_ON_RECIPIENT_UPDATE = True

# When you click send, should it check and pop up a modal dialogue box
ALERT_ON_SEND = True

# If any of the listed strings are found in the recipients array, the account will be switched to the one given.

ACCOUNTS = {
#    'Matthew Somerville <matthew@dracos.co.uk>': [ 'dracos.co.uk', 'stefan@whitelabel.org' ],
	#    'Matthew Somerville <matthew@mysociety.org>': [ 'mysociety.org', 'theyworkforyou.com', 'team@fixmystreet.com' ],
}