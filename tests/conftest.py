from pathlib import Path

import nonebot
import pytest
from nonebug import NONEBOT_INIT_KWARGS


def pytest_configure(config: pytest.Config) -> None:
    config.stash[NONEBOT_INIT_KWARGS] = {"driver": "~none"}


@pytest.fixture(scope="session")
def tmp_path(tmp_path_factory: pytest.TempPathFactory) -> Path:
    return tmp_path_factory.mktemp("nonebot_plugin_localstore")


@pytest.fixture(scope="session", autouse=True)
def after_nonebot_init(after_nonebot_init: None, tmp_path: Path):
    nonebot.load_plugin("nonebot_plugin_localstore")

    with pytest.MonkeyPatch.context() as m:
        m.setattr("nonebot_plugin_localstore.BASE_DATA_DIR", tmp_path / "data")
        m.setattr("nonebot_plugin_localstore.BASE_CACHE_DIR", tmp_path / "cache")
        m.setattr("nonebot_plugin_localstore.BASE_CONFIG_DIR", tmp_path / "config")

        m.setattr(
            "nonebot_plugin_localstore.plugin_config.localstore_plugin_data_dir",
            {"spec_plugin": tmp_path / "spec_plugin_data"},
        )
        m.setattr(
            "nonebot_plugin_localstore.plugin_config.localstore_plugin_cache_dir",
            {"spec_plugin": tmp_path / "spec_plugin_cache"},
        )
        m.setattr(
            "nonebot_plugin_localstore.plugin_config.localstore_plugin_config_dir",
            {"spec_plugin": tmp_path / "spec_plugin_config"},
        )

        nonebot.load_plugin("tests.plugin")
        nonebot.load_plugin("tests.spec_plugin")
        yield
