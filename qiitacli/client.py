#!/usr/bin/env python3

import click

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
    print("list")


@cmd.command()
def add():
    '''
    Add new article
    '''
    print("add")


def main():
    cmd()


if __name__ == '__main__':
    main()
