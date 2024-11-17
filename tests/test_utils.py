import pytest
from lib.utils import load_config
from lib.custom_exceptions import ConfigFileNotFoundError
from munch import DefaultMunch
from yaml import YAMLError


@pytest.fixture
def mock_config_file(tmpdir):
    file_path = tmpdir / "config.yaml"
    file_path.write("key: value")
    return str(file_path)


def test_load_config_success(mock_config_file):
    result = load_config(mock_config_file)
    assert isinstance(result, DefaultMunch)
    assert result.key == "value"


def test_load_config_file_not_found():
    with pytest.raises(ConfigFileNotFoundError):
        load_config("/non/existent/path/config.yaml")


def test_load_config_invalid_yaml(tmpdir):
    # Create an invalid YAML configuration file
    file_path = tmpdir / "invalid_config.yaml"
    file_path.write("key: value: another_value")  # Invalid YAML format

    # Test if the function raises a YAMLError
    with pytest.raises(YAMLError):
        load_config(file_path)
