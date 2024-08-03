from pathlib import Path


def test_plugin_dir(tmp_path: Path):
    from tests.plugin import data_dir, cache_dir, config_dir

    assert data_dir == tmp_path / "data" / "plugin"
    assert data_dir.is_dir()
    assert cache_dir == tmp_path / "cache" / "plugin"
    assert cache_dir.is_dir()
    assert config_dir == tmp_path / "config" / "plugin"
    assert config_dir.is_dir()


def test_sub_plugin_dir(tmp_path: Path):
    """获取到子插件的缓存目录、配置目录和数据目录"""
    from tests.plugin.plugins.sub_plugin import data_dir, cache_dir, config_dir

    assert data_dir == tmp_path / "data" / "plugin" / "sub_plugin"
    assert data_dir.is_dir()
    assert cache_dir == tmp_path / "cache" / "plugin" / "sub_plugin"
    assert cache_dir.is_dir()
    assert config_dir == tmp_path / "config" / "plugin" / "sub_plugin"
    assert config_dir.is_dir()
