"""Shared config loader. DTI_CONFIG env var overrides the default path."""

import os
from pathlib import Path

import yaml


def load_config() -> dict:
    path = Path(os.environ.get("DTI_CONFIG", "config/config.yaml"))
    with open(path) as f:
        return yaml.safe_load(f)
