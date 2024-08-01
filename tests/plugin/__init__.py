from pathlib import Path

import nonebot
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot import require, on_command

require("nonebot_plugin_localstore")
from nonebot_plugin_localstore import (
    get_plugin_data_dir,
    get_plugin_cache_dir,
    get_plugin_config_dir,
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


_sub_plugins = set()
_sub_plugins |= nonebot.load_plugins(str((Path(__file__).parent / "plugins").resolve()))
