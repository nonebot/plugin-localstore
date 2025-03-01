from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field


class Config(BaseModel):
    localstore_use_cwd: bool = False
    localstore_cache_dir: Optional[Path] = None
    localstore_config_dir: Optional[Path] = None
    localstore_data_dir: Optional[Path] = None

    localstore_plugin_cache_dir: dict[str, Path] = Field(default_factory=dict)
    localstore_plugin_config_dir: dict[str, Path] = Field(default_factory=dict)
    localstore_plugin_data_dir: dict[str, Path] = Field(default_factory=dict)
