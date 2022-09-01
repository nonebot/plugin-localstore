from pathlib import Path

from .data_source import user_data_dir, user_cache_dir, user_config_dir

BASE_CACHE_DIR = Path(user_cache_dir("nonebot2")).resolve()
BASE_CONFIG_DIR = Path(user_config_dir("nonebot2")).resolve()
BASE_DATA_DIR = Path(user_data_dir("nonebot2")).resolve()


def get_cache_dir(plugin_name: str) -> str:
    return str(BASE_CACHE_DIR / plugin_name)


def get_cache_file(plugin_name: str, filename: str) -> str:
    return str(BASE_CACHE_DIR / plugin_name / filename)


def get_config_dir(plugin_name: str) -> str:
    return str(BASE_CONFIG_DIR / plugin_name)


def get_config_file(plugin_name: str, filename: str) -> str:
    return str(BASE_CONFIG_DIR / plugin_name / filename)


def get_data_dir(plugin_name: str) -> str:
    return str(BASE_DATA_DIR / plugin_name)


def get_data_file(plugin_name: str, filename: str) -> str:
    return str(BASE_DATA_DIR / plugin_name / filename)
