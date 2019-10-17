import os

PRODUCT_NAME = 'qiitacli'
ACCESSTOKEN_PATH = os.environ.get(
    "QIITACLI_ACCESSTOKEN_PATH", "/path/to/etc/accesstoken.secret")

__version__ = '0.1.0'
