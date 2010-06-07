import sys
import StringIO
old_stderr = sys.stderr
sys.stderr = StringIO.StringIO()
import paramiko
sys.stderr = old_stderr
from thundercat.response import process_response

class Transport(object):
    def __init__(self, host):
        self.host = host
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def request(self, request_body, file=None):
        username, hostname = self.host.split('@', 1)
        self.client.connect(hostname, username=username)
        stdin, stdout, stderr = self.client.exec_command(request_body)
        if file:
            stdin.write(file.read())
            stdin.flush()
            stdin.channel.shutdown(2)
            results = stderr.read()
        else:
            results = stderr.read()
        return process_response(results)
