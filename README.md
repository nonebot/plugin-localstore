<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://raw.githubusercontent.com/nonebot/nonebot2/master/docs/.vuepress/public/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# NoneBot Plugin LocalStore

_✨ NoneBot 本地存储插件 ✨_

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/nonebot/plugin-localstore/master/LICENSE">
    <img src="https://img.shields.io/github/license/nonebot/plugin-localstore.svg" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot-plugin-localstore">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-localstore.svg" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="python">
</p>

## 使用方式

加载插件后使用 `require` 获取导出方法

```python
from nonebot import require

store = require("nonebot_plugin_localstore")

plugin_cache_dir = store.get_cache_dir("plugin_name")
plugin_cache_file = store.get_cache_file("plugin_name", "filename")
plugin_config_dir = store.get_config_dir("plugin_name", "filename")
plugin_config_file = store.get_config_file("plugin_name", "filename")
plugin_data_dir = store.get_data_dir("plugin_name")
plugin_data_file = store.get_data_file("plugin_name", "filename")
```

## 存储路径

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
