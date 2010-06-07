from thundercat.response import process_response
from thundercat import addhost, discover
from thundercat.ssh import Transport 
import config
import sys

def main(argv=sys.argv):
    subcommand = argv[1]
    if subcommand == 'addremote':
        addhost.add_host(argv[1:4])
        discover.discover_command(['discover', argv[2]])
    elif subcommand == 'help':
        host_info = config.get_host_info(argv[2])
        print host_info['endpoints'][argv[3]]['help_text'].replace('{EXECUTABLE}', argv[0])
    else:
        host_info = config.get_host_info(argv[1])
        if host_info:
            endpoint = host_info['endpoints'].get(argv[2], None) if len(argv) > 2 else None
            if endpoint:
                simple_regex = endpoint['regex']
                for possibility, arg_names in simple_regex:
                    response_dict = {}
                    available_args = argv[3:]
                    available_args.reverse()
                    for arg_name in arg_names:
                        parameter_type = endpoint['params'].get(arg_name, None)
                        if isinstance(parameter_type, list):
                            available_args.reverse()
                            response_dict[arg_name] = parameter_type[1].join(available_args) 
                            available_args = []
                        else:
                            try:
                                response_dict[arg_name] = available_args.pop()
                            except IndexError:
                                pass
                    try:
                        result = possibility % response_dict
                        transport = Transport(host_info['url'])
                        print transport.request(result)
                    except (TypeError, KeyError) as e:
                        pass
            else:
                print process_response({
                    'content': {
                        'message':'Bad endpoint %s\nAvailable endpoints:\n\t%s\n' % (argv[2] if len(argv) > 2 else "<none provided>", '\n\t'.join(host_info['endpoints'].keys())), 
                    },
                    'status_code':404,
                })
        else:
            print process_response({
                'content':{
                    'message':'Bad host %s\nAvailable hosts:\n\t%s\n' % (argv[1], '\n\t'.join(config.get_available_host_list())),
                },
                'status_code':404,
            })

if __name__ == '__main__':
    main(sys.argv)
