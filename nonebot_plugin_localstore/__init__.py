from pathlib import Path
from typing import Optional

from .data_source import user_data_dir, user_cache_dir, user_config_dir

APP_NAME = "nonebot2"
BASE_CACHE_DIR = user_cache_dir(APP_NAME).resolve()
BASE_CONFIG_DIR = user_config_dir(APP_NAME).resolve()
BASE_DATA_DIR = user_data_dir(APP_NAME).resolve()


def get_cache_dir(plugin_name: Optional[str]) -> Path:
    return BASE_CACHE_DIR / plugin_name if plugin_name else BASE_CACHE_DIR


def get_cache_file(plugin_name: Optional[str], filename: str) -> Path:
    return get_cache_dir(plugin_name) / filename


def get_config_dir(plugin_name: Optional[str]) -> Path:
    return BASE_CONFIG_DIR / plugin_name if plugin_name else BASE_CONFIG_DIR


def get_config_file(plugin_name: Optional[str], filename: str) -> Path:
    return get_config_dir(plugin_name) / filename


def get_data_dir(plugin_name: Optional[str]) -> Path:
    return BASE_DATA_DIR / plugin_name if plugin_name else BASE_DATA_DIR


def get_data_file(plugin_name: Optional[str], filename: str) -> Path:
    return get_data_dir(plugin_name) / filename
