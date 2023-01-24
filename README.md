<!-- markdownlint-disable MD041 -->
<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
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

plugin_cache_dir: Path = store.get_cache_dir("plugin_name")
plugin_cache_file: Path = store.get_cache_file("plugin_name", "filename")
plugin_config_dir: Path = store.get_config_dir("plugin_name", "filename")
plugin_config_file: Path = store.get_config_file("plugin_name", "filename")
plugin_data_dir: Path = store.get_data_dir("plugin_name")
plugin_data_file: Path = store.get_data_file("plugin_name", "filename")
```

## 存储路径

在项目安装插件后，可以使用 `nb-cli` 查看具体的存储路径：

```bash
nb localstore
```

参考路径如下：

### cache path

- macOS: `~/Library/Caches/<AppName>`
- Unix: `~/.cache/<AppName>` (XDG default)
- Windows: `C:\Users\<username>\AppData\Local\<AppName>\Cache`

### data path

- macOS: `~/Library/Application Support/<AppName>`
- Unix: `~/.local/share/<AppName>` or in $XDG_DATA_HOME, if defined
- Win XP (not roaming): `C:\Documents and Settings\<username>\Application Data\<AppName>`
- Win 7 (not roaming): `C:\Users\<username>\AppData\Local\<AppName>`

### config path

- macOS: same as user_data_dir
- Unix: `~/.config/<AppName>`
- Win XP (roaming): `C:\Documents and Settings\<username>\Local Settings\Application Data\<AppName>`
- Win 7 (roaming): `C:\Users\<username>\AppData\Roaming\<AppName>`
