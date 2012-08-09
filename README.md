Mail.app-AutoFromPicker-plugin
==============================

Automatically keep work and personal OS X Mail.app accounts separate.

Here, it does three things, with a bug in one of them:

1. When you hit reply to a mail, it scans the recipients and sets the From
   account accordingly.

2. When you alter the recipient lines whilst writing an email, it updates the
   From account. [1]

3. When you hit send, it does a final check of the recipients and brings up a
   dialogue box (though given 1 and 2 it probably won't have to do that, as
   it'll already be set correctly).

[1] It does do this, but it does not refresh the display of the dropdown - this
is the bug, I can't work out how to tell it to redraw. I think pre-Lion had a
call that was removed in Lion; I imagine there must be a way, but as none of
this is documented, I'm not sure how to find out.

Install
-------

If you haven't installed Mail bundles before, you might need to run the two
defaults write commands as given on http://www.cs.unc.edu/~welch/MailFollowup/
under the manual install instructions.

0. Quit Mail.
1. Clone this repository
2. Copy config.py.EXAMPLE to config.py and edit to have your account details
   and domains/emails you're interested in. Make sure the account matches what
   appears in Mail's From drop down exactly. Also pick which features you want
   to be on (True) or off (False).
3. Run make.sh in this directory. This will build the app and move it into
   Mail's Bundles directory.
4. Start Mail.

Da-da! If it doesn't work, run Console and see what error it's outputting when
it goes wrong, and let me know.
=======
Automatically keep work and personal OS X Mail.app accounts separate

Based on Attachment Scanner Plugin by James Eagan http://eaganj.free.fr/code/mail-plugin/

and the code was written by Matthew Somerville...

Installation
If you haven't installed Mail bundles before, you'll have to run the two defaults write commands as given on http://www.cs.unc.edu/~welch/MailFollowup/ install instructions.

Quit Mail.
Unzip the zip file.
Edit config.py.EXAMPLE to have your account details and domains/emails you're interested in, make sure the account matches what appears in Mail's From drop down exactly, and save as config.py
Edit the True/False depending upon which functionality you want.
Open up Terminal in the directory containing what you've just unzipped.
Run "python setup.py py2app" to create the app from the source code, it'll print some gumph.
Move the newly created dist/AutoFromPicker.mailbundle to ~/Library/Mail/Bundles/
Start Mail.
If it gives a disabled plugin error, then I missed out some Mail version UUIDs from the list you have to provide for every version of Mail you want your plugin to run under. Find yours by running:

   defaults read /System/Library/Frameworks/Message.framework/Resources/Info PluginCompatibilityUUID
   defaults read /Applications/Mail.app/Contents/Info PluginCompatibilityUUID
and adding those two strings to the list in setup.py before step 4 below (which you'll see has many strings for many different versions).

Da-da! If it doesn't work, run Console and see what error it's outputting when it goes wrong, and let me know.

Here, it does three things, with a bug in one of them:

When you hit reply to a mail, it scans the recipients and sets the From account accordingly.
When you alter the recipient lines whilst writing an email, it updates the From account. [1]
When you hit send, it does a final check of the recipients and brings up a dialogue box (though given 1 and 2 it probably won't have to do that, as it'll already be set correctly).
[1] It does do this, but it does not refresh the display of the dropdown - this is the bug, I can't work out how to tell it to redraw. I think pre-Lion had a call that was removed in Lion; I imagine there must be a way, but as none of this is documented, I'm not sure how to find out.
>>>>>>> better README.md
=======
Automatically keep work and personal OS X Mail.app accounts separate
>>>>>>> Revert "better README.md"
