from click.testing import CliRunner

from qiitacli.client import cmd


def test_client_command():
    runner = CliRunner()
    result = runner.invoke(cmd)
    print(result.output)
    assert result.exit_code == 0


def test_client_add():
    runner = CliRunner()
    result = runner.invoke(cmd, ['add', '--help'])
    print(result.output)
    assert result.exit_code == 0


def test_client_add_verbose():
    runner = CliRunner()
    result = runner.invoke(cmd, ['--verbose', 'add', '--help'])
    print(result.output)
    assert result.exit_code == 0


def test_client_list():
    runner = CliRunner()
    result = runner.invoke(cmd, ['list', '--help'])
    print(result.output)
    assert result.exit_code == 0

def test_client_status():
    runner = CliRunner()
    result = runner.invoke(cmd, ['status', '--help'])
    print(result.output)
    assert result.exit_code == 0
