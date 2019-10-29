import os

PRODUCT_NAME = 'qiitacli'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACCESSTOKEN_PATH = os.environ.get(
    "QIITACLI_ACCESSTOKEN_PATH", os.path.join(BASE_DIR, "etc", "accesstoken.secret"))

__version__ = '0.1.0'
