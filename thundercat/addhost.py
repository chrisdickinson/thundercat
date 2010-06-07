from thundercat import config
import sys

def add_host(argv=sys.argv):
    nickname, host_url = argv[1:3]
    if not config.get_host_info(nickname):
        config.set_host_info(nickname, {'url':host_url})
        print "Added %s to thundercat" % nickname
    print "%s already exists in thundercat." % nickname
