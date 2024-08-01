from pathlib import Path

import pytest
import nonebot
from nonebug.app import App
from pytest_mock import MockerFixture
from nonebug import NONEBOT_INIT_KWARGS


def pytest_configure(config: pytest.Config) -> None:
    config.stash[NONEBOT_INIT_KWARGS] = {
        "driver": "~none",
    }


@pytest.fixture(scope="session")
def _load_plugin(nonebug_init: None):
    nonebot.load_plugin("tests.plugin")


@pytest.fixture
def app(_load_plugin: None, tmp_path: Path, mocker: MockerFixture):
    # 插件数据目录
    mocker.patch("nonebot_plugin_localstore.BASE_DATA_DIR", tmp_path / "data")
    mocker.patch("nonebot_plugin_localstore.BASE_CACHE_DIR", tmp_path / "cache")
    mocker.patch("nonebot_plugin_localstore.BASE_CONFIG_DIR", tmp_path / "config")

    return App()
