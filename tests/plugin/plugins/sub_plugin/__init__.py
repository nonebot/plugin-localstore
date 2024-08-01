from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg

from nonebot_plugin_localstore import (
    get_plugin_data_dir,
    get_plugin_cache_dir,
    get_plugin_config_dir,
)

sub_plugin_cmd = on_command("sub_plugin")


@sub_plugin_cmd.handle()
async def plugin_handle(args: Message = CommandArg()):
    type_ = args.extract_plain_text()

    if type_ == "cache":
        cache_dir = get_plugin_cache_dir()
        await sub_plugin_cmd.finish(f"{cache_dir}")
    elif type_ == "config":
        config_dir = get_plugin_config_dir()
        await sub_plugin_cmd.finish(f"{config_dir}")
    elif type_ == "data":
        data_dir = get_plugin_data_dir()
        await sub_plugin_cmd.finish(f"{data_dir}")
