from pathlib import Path
from typing import Callable, Optional
from typing_extensions import ParamSpec

from nonebot import get_driver
from nonebot.plugin import PluginMetadata

from .config import Config
from .data_source import user_data_dir, user_cache_dir, user_config_dir

__plugin_meta__ = PluginMetadata(
    name="本地数据存储",
    description="存储插件数据至本地文件",
    usage=(
        '声明依赖: `require("nonebot_plugin_localstore")`\n'
        "导入所需文件夹:\n"
        '  `cache_dir = store.get_cache_dir("plugin_name")`\n'
        '  `cache_file = store.get_cache_file("plugin_name", "file_name")`\n'
        '  `data_dir = store.get_data_dir("plugin_name")`\n'
        '  `data_file = store.get_data_file("plugin_name", "file_name")`\n'
        '  `config_dir = store.get_config_dir("plugin_name")`\n'
        '  `config_file = store.get_config_file("plugin_name", "file_name")`'
    ),
    type="library",
    homepage="https://github.com/nonebot/plugin-localstore",
    config=Config,
    supported_adapters=None,
)

plugin_config = Config.parse_obj(get_driver().config)

P = ParamSpec("P")

APP_NAME = "nonebot2"
BASE_CACHE_DIR = (
    user_cache_dir(APP_NAME).resolve()
    if plugin_config.localstore_cache_dir is None
    else plugin_config.localstore_cache_dir.resolve()
)
BASE_CONFIG_DIR = (
    user_config_dir(APP_NAME).resolve()
    if plugin_config.localstore_config_dir is None
    else plugin_config.localstore_config_dir.resolve()
)
BASE_DATA_DIR = (
    user_data_dir(APP_NAME).resolve()
    if plugin_config.localstore_data_dir is None
    else plugin_config.localstore_data_dir.resolve()
)


def _ensure_dir(path: Path) -> None:
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    elif not path.is_dir():
        raise RuntimeError(f"{path} is not a directory")


def _auto_create_dir(func: Callable[P, Path]) -> Callable[P, Path]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Path:
        path = func(*args, **kwargs)
        _ensure_dir(path)
        return path

    return wrapper


@_auto_create_dir
def get_cache_dir(plugin_name: Optional[str]) -> Path:
    return BASE_CACHE_DIR / plugin_name if plugin_name else BASE_CACHE_DIR


def get_cache_file(plugin_name: Optional[str], filename: str) -> Path:
    return get_cache_dir(plugin_name) / filename


@_auto_create_dir
def get_config_dir(plugin_name: Optional[str]) -> Path:
    return BASE_CONFIG_DIR / plugin_name if plugin_name else BASE_CONFIG_DIR


def get_config_file(plugin_name: Optional[str], filename: str) -> Path:
    return get_config_dir(plugin_name) / filename


@_auto_create_dir
def get_data_dir(plugin_name: Optional[str]) -> Path:
    return BASE_DATA_DIR / plugin_name if plugin_name else BASE_DATA_DIR


def get_data_file(plugin_name: Optional[str], filename: str) -> Path:
    return get_data_dir(plugin_name) / filename
