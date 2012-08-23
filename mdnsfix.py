"""
I wrote this script to address the issue wherein Apple changed DNS search
resolution in it's Lion (and later) OS such that subdomains are not
searched.  This is fixed by modifying the arguments passed to the
mDNSResponder which is handled by launchd.

.. codeauthor:: Lou Zirkel <zzzirk@zzzirk.com>
"""

import sys
import plistlib

MDNS_PLIST = "/System/Library/LaunchDaemons/com.apple.mDNSResponder.plist"
ARG_SEARCH_DOMAINS = "-AlwaysAppendSearchDomains"


mdns = plistlib.readPlist(MDNS_PLIST)

if ARG_SEARCH_DOMAINS not in mdns['ProgramArguments']:
    mdns['ProgramArguments'].append(ARG_SEARCH_DOMAINS)
    try:
        plistlib.writePlist(mdns, MDNS_PLIST)
    except IOError, e:
        if e.errno == 13:
            print "Permissiono denied."
            sys.exit(1)
    print "mDNS search domain fix applied."
    print "You should now execute the following two commands:"
    print "    sudo launchctl unload -w %s" % (MDNS_PLIST)
    print "    sudo launchctl load -w %s" % (MDNS_PLIST)
else:
    print "mDNS search domain fix already applied."
