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
from distutils.core import setup
import py2app

# If running gives a 'disabled plugin' error, then I missed out some Mail version UUIDs from the list; you have to provide for every version of Mail you want your plugin to run under. Find yours by running:
#   "defaults read /System/Library/Frameworks/Message.framework/Resources/Info PluginCompatibilityUUID"
#   "defaults read /Applications/Mail.app/Contents/Info PluginCompatibilityUUID"
#    and adding those two strings to the list below

VERSION='0.3'
COPYRIGHT='Copyright 2012, Matthew Somerville'

plist = dict(NSPrincipalClass='AutoFromPicker',
             CFBundleGetInfoString=\
              'Auto From Picker plugin version %s, %s' % (VERSION, COPYRIGHT),
             CFBundleIdentifier='uk.co.dracos.AutoFromPicker',
             CFBundlePackageType='BNDL',
             CFBundleShortVersionString=VERSION,
#             CFBundleVersion=VERSION,
             NSHumanReadableCopyright=COPYRIGHT,
             SupportedPluginCompatibilityUUIDs=['225E0A48-2CDB-44A6-8D99-A9BB8AF6BA04', # Mail 4.0
                                                'B3F3FC72-315D-4323-BE85-7AB76090224D', # Message 4.0
                                                '2610F061-32C6-4C6B-B90A-7A3102F9B9C8', # Mail 4.1
                                                '99BB3782-6C16-4C6F-B910-25ED1C1CB38B', # Message 4.1
                                                '2F0CF6F9-35BA-4812-9CB2-155C0FDB9B0F', # Mail 4.2
                                                '0CB5F2A0-A173-4809-86E3-9317261F1745', # Message 4.2
                                                'B842F7D0-4D81-4DDF-A672-129CA5B32D57', # Mail 4.3
                                                'E71BD599-351A-42C5-9B63-EA5C47F7CE8E', # Message 4.3
                                                'BDD81F4D-6881-4A8D-94A7-E67410089EEB', # Mail 4.4
                                                '857A142A-AB81-4D99-BECC-D1B55A86D94E', # Message 4.4
                                                '1C58722D-AFBD-464E-81BB-0E05C108BE06', # 10.6.7 (4.5)
                                                '9049EF7D-5873-4F54-A447-51D722009310', # 10.6.7 (4.5)
                                                '36555EB0-53A7-4B29-9B84-6C0C6BACFC23', # Mail 4.4.1?
                                                '6E7970A3-E5F1-4C41-A904-B18D3D8FAA7D', # Mail 5.1
                                                'EF59EC5E-EFCD-4EA7-B617-6C5708397D24', # Message 5.1
                                                '4C286C70-7F18-4839-B903-6F2D58FA4C71', # Mail 5.2 (upto 10.7.4)
                                               ]
        )

setup(
    plugin = ['AutoFromPicker.py'],
    options = dict(py2app=dict(extension='.mailbundle', plist=plist))
 )  
