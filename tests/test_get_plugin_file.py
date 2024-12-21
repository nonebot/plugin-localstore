from pathlib import Path


def test_plugin_file(tmp_path: Path):
    from tests.plugin import cache_file, config_file, data_file

    assert data_file == tmp_path / "data" / "plugin" / "data_file"
    assert cache_file == tmp_path / "cache" / "plugin" / "cache_file"
    assert config_file == tmp_path / "config" / "plugin" / "config_file"


def test_spec_plugin_file(tmp_path: Path):
    from tests.spec_plugin import cache_file, config_file, data_file

    assert data_file == tmp_path / "spec_plugin_data" / "data_file"
    assert cache_file == tmp_path / "spec_plugin_cache" / "cache_file"
    assert config_file == tmp_path / "spec_plugin_config" / "config_file"


def test_sub_plugin_file(tmp_path: Path):
    from tests.plugin.plugins.sub_plugin import cache_file, config_file, data_file

    assert data_file == tmp_path / "data" / "plugin" / "sub_plugin" / "data_file"
    assert cache_file == tmp_path / "cache" / "plugin" / "sub_plugin" / "cache_file"
    assert config_file == tmp_path / "config" / "plugin" / "sub_plugin" / "config_file"


def test_spec_sub_plugin_file(tmp_path: Path):
    from tests.spec_plugin.plugins.sub_plugin import cache_file, config_file, data_file

    assert data_file == tmp_path / "spec_plugin_data" / "sub_plugin" / "data_file"
    assert cache_file == tmp_path / "spec_plugin_cache" / "sub_plugin" / "cache_file"
    assert config_file == tmp_path / "spec_plugin_config" / "sub_plugin" / "config_file"
