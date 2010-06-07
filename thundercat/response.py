import simplejson

class ResponseBase(object):
    ranges = {
        (0, 199):35,
        (200, 399):32,
        (400, 499):33,
        (500, 999):31,
    }

    def __init__(self):
        pass

    def get_color(self):
        for k in ResponseBase.ranges.keys():
            if k[0] <= self.status_code < k[1]:
                return ResponseBase.ranges[k]
        return 33

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        color = self.get_color()
        return "\033[0;%dm%s\033[0m\n" % (color, self.message)

def process_response(raw_json_info):
    info = simplejson.loads(raw_json_info) if not isinstance(raw_json_info, dict) else raw_json_info
    message = info['content']
    if isinstance(message, dict):
        message = info['content'].pop('message', '')
    info.update({
        'message':message,
    })
    return type('Response', (ResponseBase,), info)() 

