from __future__ import (absolute_import,
                        division,
                        print_function,
                        unicode_literals)

import argparse
import json
import os
import yaml


from github import Github


def ask_questions():
    org = input('Organization Name: ')

    user_info = {
        'organization': org
    }
    return user_info


def create_admin_repo(org):
    created_repo = org.create_repo(name='administrative',
                                   description='Hackweek project management.')

    with open(os.path.join(os.path.dirname(__file__), 'templates', 'README.md')) as f:
        created_repo.create_file('/README.md', message='Initialize commit',
                                 content=f.read())

    with open(os.path.join(os.path.dirname(__file__), 'templates', 'issues.yml')) as yml:
        yaml_dict = yaml.load(yml.read())

    for cont in yaml_dict['issues']:
        created_repo.create_issue(title=cont['title'],
                                  body=cont['body'],
                                  labels=cont['label'])

def get_github(credfile):
    with open(credfile) as cf:
        creds = json.load(cf)

    return Github(login_or_token=creds['username'],
                  password=creds['password'])


def cli():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('credfile', metavar='CRED', type=str, help='Credential file.')

    return parser.parse_args()


def main():
    args = cli()
    g = get_github(args.credfile)

    user_info = ask_questions()
    org = g.get_organization(login=user_info['organization'])
    create_admin_repo(org)


if __name__ == '__main__':
    main()