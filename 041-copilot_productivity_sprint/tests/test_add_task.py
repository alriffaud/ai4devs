import json
import pytest
from main import add_task

def test_add_task_creates_entry(tmp_path, monkeypatch):
    # Prepare empty config file
    config_file = tmp_path / 'config.json'
    config_file.write_text(json.dumps({"tasks": []}))
    monkeypatch.chdir(tmp_path)
    # Add a new task
    add_task("Task A", 30)
    # Load config and verify task
    data = json.loads((tmp_path / 'config.json').read_text())
    assert any(t.get("description") == "Task A" for t in data.get("tasks", [])), "Task A not found in tasks"
