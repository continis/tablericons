from __future__ import annotations

from markupsafe import Markup

import tablericons as _tablericons


def icon(name: str, *, size: int | None = 24, **kwargs: object) -> str:
    return _render_icon(name, size, **kwargs)


def _render_icon(name: str, size: int | None, **kwargs: object) -> str:
    return Markup(_tablericons._render_icon(name, size, **kwargs))
