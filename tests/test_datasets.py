import io

import pandas as pd
import pytest
import requests

from amazonasdatahub import datasets

SAMPLE = pd.DataFrame({"a": [1, 2], "b": [3.5, 4.5]})
NEWER = pd.DataFrame({"a": [9, 8], "b": [7.5, 6.5]})


def to_parquet_bytes(df):
    buffer = io.BytesIO()
    df.to_parquet(buffer)
    return buffer.getvalue()


class FakeResponse:
    def __init__(self, content=b"", error=None):
        self.content = content
        self._error = error

    def raise_for_status(self):
        if self._error:
            raise self._error


@pytest.fixture(autouse=True)
def cache_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(datasets, "CACHE_DIR", tmp_path)
    return tmp_path


def test_downloads_when_cache_is_empty(cache_dir, monkeypatch, capsys):
    monkeypatch.setattr(
        datasets.requests, "get", lambda url: FakeResponse(to_parquet_bytes(SAMPLE))
    )

    result = datasets.get_dataset("sample")

    pd.testing.assert_frame_equal(result, SAMPLE)
    assert (cache_dir / "sample.parquet").exists()
    assert "Saved in" in capsys.readouterr().out


def test_uses_cache_without_downloading(cache_dir, monkeypatch):
    SAMPLE.to_parquet(cache_dir / "sample.parquet")

    def fail(url):
        raise AssertionError("requests.get should not be called")

    monkeypatch.setattr(datasets.requests, "get", fail)

    pd.testing.assert_frame_equal(datasets.get_dataset("sample"), SAMPLE)


def test_force_downloads_again(cache_dir, monkeypatch):
    SAMPLE.to_parquet(cache_dir / "sample.parquet")
    monkeypatch.setattr(
        datasets.requests, "get", lambda url: FakeResponse(to_parquet_bytes(NEWER))
    )

    result = datasets.get_dataset("sample", force=True)

    pd.testing.assert_frame_equal(result, NEWER)


def test_download_error_without_cache_raises(monkeypatch):
    def boom(url):
        raise requests.ConnectionError("offline")

    monkeypatch.setattr(datasets.requests, "get", boom)

    with pytest.raises(Exception, match="no cache available"):
        datasets.get_dataset("sample")


def test_http_error_without_cache_raises(monkeypatch):
    monkeypatch.setattr(
        datasets.requests,
        "get",
        lambda url: FakeResponse(error=requests.HTTPError("404")),
    )

    with pytest.raises(Exception, match="no cache available"):
        datasets.get_dataset("sample")


def test_download_error_with_cache_uses_old_version(cache_dir, monkeypatch, capsys):
    SAMPLE.to_parquet(cache_dir / "sample.parquet")

    def boom(url):
        raise requests.ConnectionError("offline")

    monkeypatch.setattr(datasets.requests, "get", boom)

    result = datasets.get_dataset("sample", force=True)

    pd.testing.assert_frame_equal(result, SAMPLE)
    assert "Warning" in capsys.readouterr().out
