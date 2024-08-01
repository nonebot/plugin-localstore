from pathlib import Path

import nonebot
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot import require, on_command

require("nonebot_plugin_localstore")
from nonebot_plugin_localstore import (
    get_plugin_data_dir,
    get_plugin_cache_dir,
    get_plugin_data_file,
    get_plugin_cache_file,
    get_plugin_config_dir,
    get_plugin_config_file,
)

plugin_cmd = on_command("plugin")


@plugin_cmd.handle()
async def plugin_handle(args: Message = CommandArg()):
    type_ = args.extract_plain_text()

    if type_ == "cache":
        cache_dir = get_plugin_cache_dir()
        await plugin_cmd.finish(f"{cache_dir}")
    elif type_ == "config":
        config_dir = get_plugin_config_dir()
        await plugin_cmd.finish(f"{config_dir}")
    elif type_ == "data":
        data_dir = get_plugin_data_dir()
        await plugin_cmd.finish(f"{data_dir}")


plugin_file_cmd = on_command("plugin_file")


@plugin_file_cmd.handle()
async def plugin_file_handle(args: Message = CommandArg()):
    type_, filename = args.extract_plain_text().split()

    if type_ == "cache":
        cache_file = get_plugin_cache_file(filename)
        await plugin_file_cmd.finish(f"{cache_file}")
    elif type_ == "config":
        config_file = get_plugin_config_file(filename)
        await plugin_file_cmd.finish(f"{config_file}")
    elif type_ == "data":
        data_file = get_plugin_data_file(filename)
        await plugin_file_cmd.finish(f"{data_file}")


_sub_plugins = set()
_sub_plugins |= nonebot.load_plugins(str((Path(__file__).parent / "plugins").resolve()))
