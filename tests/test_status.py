from click.testing import CliRunner
from qiitacli.client import cmd

from . import load_accesstoken, write_accesstoken, remove_accesstoken

def test_status():
    token = load_accesstoken()
    write_accesstoken(token)
    runner = CliRunner()
    result = runner.invoke(cmd, ['status'])
    print(result.output)
    assert result.exit_code == 0
    remove_accesstoken()
