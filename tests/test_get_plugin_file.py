from pathlib import Path

from nonebug import App

from tests.utils import make_fake_event, make_fake_message


async def test_plugin_file(app: App, tmp_path: Path):
    """获取到插件的缓存文件、配置文件和数据文件"""
    from tests.plugin import plugin_file_cmd

    async with app.test_matcher(plugin_file_cmd) as ctx:
        bot = ctx.create_bot()
        message = make_fake_message()("/plugin_file cache cache_file")
        event = make_fake_event(_message=message)()

        ctx.receive_event(bot, event)
        ctx.should_call_send(
            event,
            str(tmp_path / "cache" / "plugin" / "cache_file"),
            True,
        )
        ctx.should_finished(plugin_file_cmd)

        message = make_fake_message()("/plugin_file config config_file")
        event = make_fake_event(_message=message)()

        ctx.receive_event(bot, event)
        ctx.should_call_send(
            event,
            str(tmp_path / "config" / "plugin" / "config_file"),
            True,
        )
        ctx.should_finished(plugin_file_cmd)

        message = make_fake_message()("/plugin_file data data_file")
        event = make_fake_event(_message=message)()

        ctx.receive_event(bot, event)
        ctx.should_call_send(
            event,
            str(tmp_path / "data" / "plugin" / "data_file"),
            True,
        )
        ctx.should_finished(plugin_file_cmd)


async def test_sub_plugin_file(app: App, tmp_path: Path):
    """获取到子插件的缓存文件、配置文件和数据文件"""
    from tests.plugin.plugins.sub_plugin import sub_plugin_file_cmd

    async with app.test_matcher(sub_plugin_file_cmd) as ctx:
        bot = ctx.create_bot()
        message = make_fake_message()("/sub_plugin_file cache cache_file")
        event = make_fake_event(_message=message)()

        ctx.receive_event(bot, event)
        ctx.should_call_send(
            event,
            str(tmp_path / "cache" / "plugin" / "sub_plugin" / "cache_file"),
            True,
        )
        ctx.should_finished(sub_plugin_file_cmd)

        message = make_fake_message()("/sub_plugin_file config config_file")
        event = make_fake_event(_message=message)()

        ctx.receive_event(bot, event)
        ctx.should_call_send(
            event,
            str(tmp_path / "config" / "plugin" / "sub_plugin" / "config_file"),
            True,
        )
        ctx.should_finished(sub_plugin_file_cmd)

        message = make_fake_message()("/sub_plugin_file data data_file")
        event = make_fake_event(_message=message)()

        ctx.receive_event(bot, event)
        ctx.should_call_send(
            event,
            str(tmp_path / "data" / "plugin" / "sub_plugin" / "data_file"),
            True,
        )
        ctx.should_finished(sub_plugin_file_cmd)
