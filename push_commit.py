import subprocess
import requests

SENTRY_API_TOKEN = 'a1b785b318374e1dbfdc5f4b9b920b93a207a97007864685acb489d2937c2ee4'


log = subprocess.Popen([
    'git',
    '--no-pager',
    'log',
    '--no-merges',
    '--no-color',
    '--pretty=%H'

], stdout=subprocess.PIPE)

commits = log.stdout.read().decode().strip().split('\n')

data = {
    'commits': [{'id': c, 'repository': 'abhijo89/feb19'} for c in commits],
    'version': 'v1.0.23',
    'projects': ['demo-django', ],
}

res = requests.post(
    'https://sentry.io/api/0/organizations/unicourt-demo/releases/',
    json=data,
    headers={'Authorization': 'Bearer {}'.format(SENTRY_API_TOKEN)},
)

