I wrote this script to address the issue wherein Apple changed DNS search
resolution in it's Lion (and later) OS such that subdomains are not
searched.  This is fixed by modifying the arguments passed to the
mDNSResponder which is handled by launchd.

