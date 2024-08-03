from pathlib import Path

import pytest
import nonebot
from nonebug import NONEBOT_INIT_KWARGS


def pytest_configure(config: pytest.Config) -> None:
    config.stash[NONEBOT_INIT_KWARGS] = {"driver": "~none"}


@pytest.fixture(scope="session")
def tmp_path(tmp_path_factory: pytest.TempPathFactory) -> Path:
    return tmp_path_factory.mktemp("nonebot_plugin_localstore")


@pytest.fixture(scope="session", autouse=True)
def _load_plugin(nonebug_init: None, tmp_path: Path):
    nonebot.load_plugin("nonebot_plugin_localstore")

    with pytest.MonkeyPatch.context() as m:
        m.setattr("nonebot_plugin_localstore.BASE_DATA_DIR", tmp_path / "data")
        m.setattr("nonebot_plugin_localstore.BASE_CACHE_DIR", tmp_path / "cache")
        m.setattr("nonebot_plugin_localstore.BASE_CONFIG_DIR", tmp_path / "config")

        nonebot.load_plugin("tests.plugin")
        yield
