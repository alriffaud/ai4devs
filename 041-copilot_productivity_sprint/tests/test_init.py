import os
import pytest
from main import init

def test_init_creates_config(tmp_path, monkeypatch):
    # Set working directory to temp
    monkeypatch.chdir(tmp_path)
    # Run init function
    init()
    # Assert config.json is created
    assert os.path.exists("config.json"), "config.json was not created by init()"
