from pathlib import Path
from typing import Optional

from pydantic import BaseModel


class Config(BaseModel):
    localstore_cache_dir: Optional[Path] = None
    localstore_config_dir: Optional[Path] = None
    localstore_data_dir: Optional[Path] = None
