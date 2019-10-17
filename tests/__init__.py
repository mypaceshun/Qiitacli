import os

BASE_DIR = os.path.abspath(__file__)
TEST_ACCESSTOKEN_PATH = os.path.join('tests', '.accesstoken.secret')
os.environ['QIITACLI_ACCESSTOKEN_PATH'] = TEST_ACCESSTOKEN_PATH
