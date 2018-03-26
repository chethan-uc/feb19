import subprocess
import requests
import raven
import os

SENTRY_API_TOKEN = 'a1b785b318374e1dbfdc5f4b9b920b93a207a97007864685acb489d2937c2ee4'


def write_sha():
    sha = raven.fetch_git_sha(os.getcwd())
    with open('__sha.txt', 'w') as f:
        f.write(sha)


def get_all_commit_list():

    try:
        with open('__sha.txt') as f:
            sha_of_previous_release = f.readline()

        log = subprocess.Popen([
            'git',
            '--no-pager',
            'log',
            '--no-merges',
            '--no-color',
            '--pretty=%H',
            '%s..HEAD' % (sha_of_previous_release,),
        ], stdout=subprocess.PIPE)
    except IOError:
        log = subprocess.Popen([
            'git',
            '--no-pager',
            'log',
            '--no-merges',
            '--no-color',
            '--pretty=%H'
        ], stdout=subprocess.PIPE)

    return log.stdout.read().decode().strip().split('\n')


def post_data():
    commits = get_all_commit_list()
    data = {
        'commits': [{'id': c, 'repository': 'abhijo89/feb19'} for c in commits],
        'version': 'v1.0.24',
        'projects': ['demo-django', ],
    }

    res = requests.post(
        'https://sentry.io/api/0/organizations/unicourt-demo/releases/',
        json=data,
        headers={'Authorization': 'Bearer {}'.format(SENTRY_API_TOKEN)},
    )
    print(res.json())
    write_sha()

post_data()