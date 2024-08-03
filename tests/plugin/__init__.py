from pathlib import Path

import nonebot

from nonebot_plugin_localstore import (
    get_plugin_data_dir,
    get_plugin_cache_dir,
    get_plugin_data_file,
    get_plugin_cache_file,
    get_plugin_config_dir,
    get_plugin_config_file,
)

data_dir = get_plugin_data_dir()
cache_dir = get_plugin_cache_dir()
config_dir = get_plugin_config_dir()

data_file = get_plugin_data_file("data_file")
cache_file = get_plugin_cache_file("cache_file")
config_file = get_plugin_config_file("config_file")

_sub_plugins = set()
_sub_plugins |= nonebot.load_plugins(str((Path(__file__).parent / "plugins").resolve()))
