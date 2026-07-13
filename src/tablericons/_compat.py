from __future__ import annotations

from importlib.resources import files
from typing import IO


def open_binary(pkg: str, filename: str) -> IO[bytes]:
    return (files(pkg) / filename).open("rb")
