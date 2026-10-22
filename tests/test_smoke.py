import pathlib
import numpy as np
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_numpy_works():
    a = np.arange(6).reshape(2, 3)
    assert a.shape == (2, 3)
    assert a.T.shape == (3, 2)


def test_thirteen_weeks_exist():
    weeks = sorted(p for p in (ROOT / "weeks").glob("w[0-9][0-9]") if p.is_dir())
    assert len(weeks) == 13, f"expected 13 week dirs, got {len(weeks)}"


@pytest.mark.skipif(not (ROOT / "weeks" / "w01" / "README.md").exists(), reason="w01 missing")
def test_week1_has_contract():
    text = (ROOT / "weeks" / "w01" / "README.md").read_text(encoding="utf-8")
    assert "周日 21:00 前" in text
