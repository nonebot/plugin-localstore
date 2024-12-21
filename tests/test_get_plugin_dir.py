from pathlib import Path


def test_plugin_dir(tmp_path: Path):
    from tests.plugin import cache_dir, config_dir, data_dir

    assert data_dir == tmp_path / "data" / "plugin"
    assert data_dir.is_dir()
    assert cache_dir == tmp_path / "cache" / "plugin"
    assert cache_dir.is_dir()
    assert config_dir == tmp_path / "config" / "plugin"
    assert config_dir.is_dir()


def test_spec_plugin_dir(tmp_path: Path):
    from tests.spec_plugin import cache_dir, config_dir, data_dir

    assert data_dir == tmp_path / "spec_plugin_data"
    assert data_dir.is_dir()
    assert cache_dir == tmp_path / "spec_plugin_cache"
    assert cache_dir.is_dir()
    assert config_dir == tmp_path / "spec_plugin_config"
    assert config_dir.is_dir()


def test_sub_plugin_dir(tmp_path: Path):
    from tests.plugin.plugins.sub_plugin import cache_dir, config_dir, data_dir

    assert data_dir == tmp_path / "data" / "plugin" / "sub_plugin"
    assert data_dir.is_dir()
    assert cache_dir == tmp_path / "cache" / "plugin" / "sub_plugin"
    assert cache_dir.is_dir()
    assert config_dir == tmp_path / "config" / "plugin" / "sub_plugin"
    assert config_dir.is_dir()


def test_spec_sub_plugin_dir(tmp_path: Path):
    from tests.spec_plugin.plugins.sub_plugin import cache_dir, config_dir, data_dir

    assert data_dir == tmp_path / "spec_plugin_data" / "sub_plugin"
    assert data_dir.is_dir()
    assert cache_dir == tmp_path / "spec_plugin_cache" / "sub_plugin"
    assert cache_dir.is_dir()
    assert config_dir == tmp_path / "spec_plugin_config" / "sub_plugin"
    assert config_dir.is_dir()
