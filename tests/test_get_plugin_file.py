from pathlib import Path


def test_plugin_file(tmp_path: Path):
    """获取到插件的缓存文件、配置文件和数据文件"""
    from tests.plugin import data_file, cache_file, config_file

    assert data_file == tmp_path / "data" / "plugin" / "data_file"
    assert cache_file == tmp_path / "cache" / "plugin" / "cache_file"
    assert config_file == tmp_path / "config" / "plugin" / "config_file"


def test_sub_plugin_file(tmp_path: Path):
    """获取到子插件的缓存文件、配置文件和数据文件"""
    from tests.plugin.plugins.sub_plugin import data_file, cache_file, config_file

    assert data_file == tmp_path / "data" / "plugin" / "sub_plugin" / "data_file"
    assert cache_file == tmp_path / "cache" / "plugin" / "sub_plugin" / "cache_file"
    assert config_file == tmp_path / "config" / "plugin" / "sub_plugin" / "config_file"
