from pathlib import Path
from typing import Optional

from pydantic import Extra, BaseModel


class Config(BaseModel, extra=Extra.ignore):
    localstore_cache_dir: Optional[Path] = None
    localstore_config_dir: Optional[Path] = None
    localstore_data_dir: Optional[Path] = None
