from click.testing import CliRunner
from qiitacli.client import cmd

def test_client_command():
    runner = CliRunner()
    result = runner.invoke(cmd)
    assert result.exit_code == 0

def test_client_add():
    runner = CliRunner()
    result = runner.invoke(cmd, 'add')
    assert result.exit_code == 0

def test_client_add_verbose():
    runner = CliRunner()
    result = runner.invoke(cmd, ['--verbose', 'add'])
    print(result.output)
    assert result.exit_code == 0

def test_client_list():
    runner = CliRunner()
    result = runner.invoke(cmd, 'list')
    assert result.exit_code == 0
