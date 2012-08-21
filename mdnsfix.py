"""
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
else:
    print "mDNS search domain fix already applied."
