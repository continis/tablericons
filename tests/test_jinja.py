from __future__ import annotations

from jinja2 import DictLoader
from jinja2 import Environment

from tablericons.jinja import icon


def make_environment(index_template: str) -> Environment:
    env = Environment(loader=DictLoader({"index": index_template}))
    env.globals.update(
        {
            "icon": icon,
        }
    )
    return env


def test_success_icon():
    env = make_environment('{{ icon("outline/x") }}')
    template = env.get_template("index")

    result = template.render()

    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M18 6l-12 12" />\n  <path d="M6 6l12 12" />\n</svg>'
        # fmt: on
    )


def test_success_icon_path_attr():
    env = make_environment('{{ icon("outline/x", stroke_linecap="butt") }}')
    template = env.get_template("index")

    result = template.render()

    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M18 6l-12 12" stroke-linecap="butt" />\n  <path d="M6 6l12 12" stroke-linecap="butt" />\n</svg>'
        # fmt: on
    )


def test_success_icon_complete():
    env = make_environment(
        '{{ icon("outline/x", size=48, class="h-4 w-4", ' + 'data_test="a < 2") }}'
    )
    template = env.get_template("index")

    result = str(template.render())

    assert result == (
        # fmt: off
        '<svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" data-test="a &lt; 2">\n  <path d="M18 6l-12 12" />\n  <path d="M6 6l12 12" />\n</svg>'
        # fmt: on
    )


def test_success_icon_size_none():
    env = make_environment('{{ icon("outline/x", size=None) }}')
    template = env.get_template("index")

    result = template.render()

    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M18 6l-12 12" />\n  <path d="M6 6l12 12" />\n</svg>'
        # fmt: on
    )
