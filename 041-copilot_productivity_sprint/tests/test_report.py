import json
import pytest
from main import report

def test_report_output(tmp_path, capsys, monkeypatch):
    # Prepare config with one task
    data = {"tasks": [{"description": "Task A", "estimate": 30, "actual": 35}]}
    (tmp_path / 'config.json').write_text(json.dumps(data))
    monkeypatch.chdir(tmp_path)
    # Run report and capture output
    report()
    captured = capsys.readouterr()
    assert "Task A" in captured.out
    assert "Estimate:" in captured.out
    assert "Actual:" in captured.out
