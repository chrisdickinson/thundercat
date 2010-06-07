from thundercat import config
from thundercat.ssh import Transport 
from thundercat.regex_helper import normalize
import sys

def process_endpoints(ep):
    output = {}
    for endpoint in ep.keys():
        output[endpoint] = {}
        output[endpoint].update(ep[endpoint])
        output[endpoint]['regex'] = normalize(ep[endpoint]['regex'])
    return output

def discover(host_url, transport=Transport):
    response = transport(host_url).request('discover')
    if response.status_code == 200:
        endpoints = response.content['endpoints']
        return response, {'url':host_url, 'endpoints':process_endpoints(endpoints)}
    else:
        return response, {}

def discover_command(argv=sys.argv):
    host_info = config.get_host_info(argv[1])
    response, info = discover(host_info['url'])
    if info:
        config.set_host_info(argv[1], info)
    print response
