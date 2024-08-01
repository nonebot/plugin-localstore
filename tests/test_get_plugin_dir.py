from pathlib import Path

from nonebug import App

from tests.utils import make_fake_event, make_fake_message


async def test_plugin_dir(app: App, tmp_path: Path):
    """获取到插件的缓存目录、配置目录和数据目录"""
    from tests.plugin import plugin_cmd

    async with app.test_matcher(plugin_cmd) as ctx:
        bot = ctx.create_bot()
        message = make_fake_message()("/plugin cache")
        event = make_fake_event(_message=message)()

        ctx.receive_event(bot, event)
        ctx.should_call_send(
            event,
            str(tmp_path / "cache" / "plugin"),
            True,
        )
        ctx.should_finished(plugin_cmd)

        message = make_fake_message()("/plugin config")
        event = make_fake_event(_message=message)()

        ctx.receive_event(bot, event)
        ctx.should_call_send(
            event,
            str(tmp_path / "config" / "plugin"),
            True,
        )
        ctx.should_finished(plugin_cmd)

        message = make_fake_message()("/plugin data")
        event = make_fake_event(_message=message)()

        ctx.receive_event(bot, event)
        ctx.should_call_send(
            event,
            str(tmp_path / "data" / "plugin"),
            True,
        )
        ctx.should_finished(plugin_cmd)


async def test_sub_plugin_dir(app: App, tmp_path: Path):
    """获取到子插件的缓存目录、配置目录和数据目录"""
    from tests.plugin.plugins.sub_plugin import sub_plugin_cmd

    async with app.test_matcher(sub_plugin_cmd) as ctx:
        bot = ctx.create_bot()
        message = make_fake_message()("/sub_plugin cache")
        event = make_fake_event(_message=message)()

        ctx.receive_event(bot, event)
        ctx.should_call_send(
            event,
            str(tmp_path / "cache" / "plugin" / "sub_plugin"),
            True,
        )
        ctx.should_finished(sub_plugin_cmd)

        message = make_fake_message()("/sub_plugin config")
        event = make_fake_event(_message=message)()

        ctx.receive_event(bot, event)
        ctx.should_call_send(
            event,
            str(tmp_path / "config" / "plugin" / "sub_plugin"),
            True,
        )
        ctx.should_finished(sub_plugin_cmd)

        message = make_fake_message()("/sub_plugin data")
        event = make_fake_event(_message=message)()

        ctx.receive_event(bot, event)
        ctx.should_call_send(
            event,
            str(tmp_path / "data" / "plugin" / "sub_plugin"),
            True,
        )
        ctx.should_finished(sub_plugin_cmd)
