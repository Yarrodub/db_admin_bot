from functools import lru_cache
from os import getcwd
from typing import TypeVar, Type

from pydantic import BaseModel, SecretStr, MySQLDsn
from ruamel.yaml import YAML


ConfigType = TypeVar('ConfigType', bound=BaseModel)


class BotConfig(BaseModel):
    token: SecretStr
    admin_id: int


class DbConfig(BaseModel):
    dsn: MySQLDsn
    is_echo: bool


@lru_cache(maxsize=1)
def parse_config_file() -> dict:
    file_path = getcwd() + '/secrets/config.yml'
    if file_path is None:
        error = 'Could not find settings file'
        raise ValueError(error)
    with open(file_path, 'rb') as file:
        yaml = YAML(typ='safe')
        config_data = yaml.load(file)
    return config_data

@lru_cache
def get_config(model: Type[ConfigType], root_key: str) -> ConfigType:
    config_dict = parse_config_file()
    if root_key not in config_dict:
        error = f'Key {root_key} not found'
        raise ValueError(error)
    return model.model_validate(config_dict[root_key])
