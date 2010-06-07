import os
import subprocess
def main(host_nickname, host_info, response):
    if response.status_code == 200:
        git_repo = os.path.join(os.getcwd(), '.git')
        if os.path.isdir(git_repo):
            try:
                result = raw_input("Would you like to add a remote to your git repo? [Y,y,n,N]").upper()[0]
                if result == 'Y':
                    git_result = subprocess.call([
                        'git', 'remote', 'add', host_nickname, ':'.join([host_info['url'], response.content['clone_path']])
                    ])
                    if git_result == 0:
                        response.message = "You successfully created the repo '%s' and added a remote named '%s'" % (response.content['clone_path'], host_nickname)

            except IndexError:
                pass
    return response
