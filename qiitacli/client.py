#!/usr/bin/env python3

import click
from qiita_v2.client import QiitaClient

from qiitacli.accesstoken import get_accesstoken

VERBOSE = False


@click.group()
@click.option('--verbose', '-v', is_flag=True)
def cmd(verbose):
    global VERBOSE
    if verbose:
        VERBOSE = verbose


@cmd.command()
def list():
    '''
    List your article
    '''
    token = get_accesstoken()
    client = QiitaClient(access_token=token)
    res = client.get_authenticated_user_items()

    str_header = 'date | url | title | tags\n'
    str_format = '{date} | {url} | {title} | {tags}\n'
    output_str = str_header

    for article in res.to_json():
        date = article['updated_at']
        url = article['url']
        title = article['title']
        tags_list = [t['name'] for t in article['tags']]
        tags = ','.join(tags_list)
        output_str += str_format.format(date=date,
                                        url=url,
                                        title=title,
                                        tags=tags)
    click.echo(output_str)


@cmd.command()
def add():
    '''
    Add new article
    '''
    print("add")


@cmd.command()
def status():
    '''
    Show authenticated user data
    '''
    token = get_accesstoken()
    client = QiitaClient(access_token=token)
    res = client.get_authenticated_user()
    output_str = '''id              : {id}
name            : {name}
location        : {location}
description     : {description}
followees_count : {followees_count}
followers_count : {followers_count}
items_count     : {items_count}
facebook_id     : {facebook_id}
github_name     : {github_login_name}
linkedin_id     : {linkedin_id}
twitter_name    : {twitter_screen_name}
'''.format(**res.to_json())
    click.echo(output_str)
