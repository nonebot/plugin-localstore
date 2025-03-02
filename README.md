<!-- markdownlint-disable MD041 -->
<p align="center">
  <a href="https://nonebot.dev/"><img src="https://nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# NoneBot Plugin LocalStore

<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD036 -->
_✨ NoneBot 本地数据存储插件 ✨_
<!-- prettier-ignore-end -->

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/nonebot/plugin-localstore/master/LICENSE">
    <img src="https://img.shields.io/github/license/nonebot/plugin-localstore.svg" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot-plugin-localstore">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-localstore.svg" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
</p>

## 使用方式

加载插件后使用 `require` 声明插件依赖，直接使用 `localstore` 插件提供的函数即可。

```python
from pathlib import Path
from nonebot import require

require("nonebot_plugin_localstore")

import nonebot_plugin_localstore as store

plugin_cache_dir: Path = store.get_plugin_cache_dir()
plugin_cache_file: Path = store.get_plugin_cache_file("filename")
plugin_config_dir: Path = store.get_plugin_config_dir()
plugin_config_file: Path = store.get_plugin_config_file("filename")
plugin_data_dir: Path = store.get_plugin_data_dir()
plugin_data_file: Path = store.get_plugin_data_file("filename")
```

## 存储路径

在项目安装插件后，可以使用 `nb-cli` 查看具体的存储路径：

```bash
nb localstore
```

参考路径如下：

当 `LOCALSTORE_USE_CWD` 为 true 时:

- cache path: `<current_working_dir>/cache/`
- data path: `<current_working_dir>/data/`
- config path: `<current_working_dir>/config/`

(`current_working_dir` 一般为 nonebot 实例的运行目录)

当 `LOCALSTORE_USE_CWD` 为 false / 未配置时:

### cache path

- macOS: `~/Library/Caches/nonebot2`
- Unix: `~/.cache/nonebot2` (XDG default)
- Windows: `C:\Users\<username>\AppData\Local\nonebot2\Cache`

### data path

- macOS: `~/Library/Application Support/nonebot2`
- Unix: `~/.local/share/nonebot2` or in $XDG_DATA_HOME, if defined
- Win XP (not roaming): `C:\Documents and Settings\<username>\Application Data\nonebot2`
- Win 7 (not roaming): `C:\Users\<username>\AppData\Local\nonebot2`

### config path

- macOS: same as user_data_dir
- Unix: `~/.config/nonebot2`
- Win XP (roaming): `C:\Documents and Settings\<username>\Local Settings\Application Data\nonebot2`
- Win 7 (roaming): `C:\Users\<username>\AppData\Roaming\nonebot2`

## 配置项

插件支持配置全局存储路径，也支持为插件单独配置存储路径。

```dotenv
LOCALSTORE_CACHE_DIR=/tmp/cache
LOCALSTORE_DATA_DIR=/tmp/data
LOCALSTORE_CONFIG_DIR=/tmp/config

LOCALSTORE_PLUGIN_CACHE_DIR='
{
  "plugin1": "/tmp/plugin1/cache",
  "plugin2:sub_plugin": "/tmp/plugin2/sub_plugin/cache"
}
'
LOCALSTORE_PLUGIN_DATA_DIR='
{
  "plugin1": "/tmp/plugin1/data",
  "plugin2:sub_plugin": "/tmp/plugin2/sub_plugin/data"
}
'
LOCALSTORE_PLUGIN_CONFIG_DIR='
{
  "plugin1": "/tmp/plugin1/config",
  "plugin2:sub_plugin": "/tmp/plugin2/sub_plugin/config"
}
'
```
