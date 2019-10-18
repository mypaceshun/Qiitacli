#!/usr/bin/env python3

import click
from qiita_v2.client import QiitaClient

from qiitacli.accesstoken import get_accesstoken

VERBOSE = False


@click.group()
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
def cmd(verbose):
    global VERBOSE
    if verbose:
        VERBOSE = verbose


@cmd.command()
@click.option('--id', '-i', is_flag=True, help='Show with article id')
@click.option('--date', '-d', is_flag=True, help='Show with article update date')  # noqa E501
@click.option('--tags', '-t', is_flag=True, help='Show with article tags')
@click.option('--url', '-u', is_flag=True, help='Show with article url')
@click.option('--separator', '-s', help='separator')
def list(id, date, tags, url, separator):
    '''
    List your article
    '''
    token = get_accesstoken()
    client = QiitaClient(access_token=token)
    res = client.get_authenticated_user_items()

    str_header = ''
    str_format = ''
    if separator is None:
        separator = '|'
    if id:
        str_header += 'id' + separator
        str_format += '{id}' + separator
    if date:
        str_header += 'date' + separator
        str_format += '{date}' + separator
    str_header += 'title'
    str_format += '{title}'
    if tags:
        str_header += separator + 'tags'
        str_format += separator + '{tags}'
    if url:
        str_header += separator + 'url'
        str_format += separator + '{url}'
    str_header += '\n'
    str_format += '\n'

    output_str = str_header

    for article in res.to_json():
        id = article['id']
        date = article['updated_at']
        url = article['url']
        title = article['title']
        tags_list = [t['name'] for t in article['tags']]
        tags = ','.join(tags_list)
        output_str += str_format.format(id=id,
                                        date=date,
                                        url=url,
                                        title=title,
                                        tags=tags)
    click.echo(output_str)


@cmd.command()
@click.argument('title', required=True)
@click.argument('article', required=True, type=click.File('r'))  # noqa E501
@click.option('--private', '-p', is_flag=True, help='Private article')
@click.option('--tags', '-t', multiple=True, help='Article tags')
@click.option('--tweet', '-T', is_flag=True, help='Tweet when article upload[Require Twitter linkage settnigs]')  # noqa E501
def upload(title, article, private, tags, tweet):
    '''
    Upload new article
    '''

    body = ''.join(article.readlines())
    click.echo(title)
    click.echo(body)


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
