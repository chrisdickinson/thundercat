import os
import simplejson
import glob
def get_config_dir():
    return os.path.expanduser('~/.thundercat')

def get_host_file(nickname):
    return os.path.join(get_config_dir(), '%s.json' % nickname)

def ensure_config_dir_exists(func):
    def inner(*args, **kwargs):
        if not os.path.exists(get_config_dir()):
            os.makedirs(get_config_dir())
        return func(*args, **kwargs)
    return inner

@ensure_config_dir_exists
def get_host_info(nickname):
    try:
        with open(get_host_file(nickname), 'r') as input:
            raw_json = input.read()
        return simplejson.loads(raw_json)
    except (ValueError, IOError) as e:
        return {}

@ensure_config_dir_exists
def set_host_info(nickname, info):
    try:
        with open(get_host_file(nickname), 'w') as output:
            output.write(simplejson.dumps(info))
        return True
    except (IOError, ValueError) as e:
        return False

@ensure_config_dir_exists
def get_available_host_list():
    for file in glob.glob(get_host_file('*')):
        yield os.path.basename(file)[:-5]
