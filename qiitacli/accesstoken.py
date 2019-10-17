import os
from pathlib import Path

from qiitacli import ACCESSTOKEN_PATH
from qiitacli.exceptions import QiitaCliException


def get_accesstoken():
    '''
    get accesstoken from ACCESSTOKEN_PATH
    When accesstoken is not set, Accesstoken read from stdin.

    Returns:
        str: AccessToken

    Exceptions:
        QiitaCliException
    '''

    tokenpath = Path(ACCESSTOKEN_PATH)

    if not tokenpath.exists():
        set_accesstoken()

    try:
        with tokenpath.open('r') as f:
            token = f.readline()
            return token
    except OSError as err:
        msg = 'AccessToken file Read Error: {}'.format(err)
        raise QiitaCliException(msg)


def set_accesstoken(token=None):
    '''
    set accesstoken
    When token is None, Accesstoken read from stdin.

    Args:
        token str: AccessToken
    '''

    tokenpath = Path(ACCESSTOKEN_PATH)

    if token is None:
        token = _read_accesstoken_from_stdin()

    try:
        curr_umask = os.umask('277')
        with tokenpath.open('w') as f:
            f.write(token.strip())
        os.umask(curr_umask)
    except OSError as err:
        msg = 'AccessToken file Write Error: {}'.format(err)
        raise QiitaCliException(msg)


def _read_accesstoken_from_stdin():
    '''
    read accesstoken from stdin

    Returns:
        str: AccessToken
    '''

    msg = 'Input your personal accesstoken: '
    try:
        token = input(msg)
    except EOFError as err:
        msg = 'AccessToken Input Error: {}'.format(err)
        raise QiitaCliException(msg)
    return token
