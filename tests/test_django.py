from __future__ import annotations

from typing import Any

import django
from django.conf import settings
from django.template import Context
from django.template import Template

settings.configure(
    ROOT_URLCONF=__name__,  # Make this module the urlconf
    SECRET_KEY="insecure",
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "APP_DIRS": False,
        },
    ],
    INSTALLED_APPS=["tablericons"],
)
urlpatterns: list[Any] = []
django.setup()


def test_success_icon():
    template = Template('{% load tablericons %}{% icon "outline/x" %}')

    result = template.render(Context())
    print(result)
    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M18 6l-12 12" />\n  <path d="M6 6l12 12" />\n</svg>'
        # fmt: on
    )


def test_success_icon_path_attr():
    template = Template(
        "{% load tablericons %}" + '{% icon "outline/x" stroke_linecap="butt" %}'
    )

    result = template.render(Context())

    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M18 6l-12 12" stroke-linecap="butt" />\n  <path d="M6 6l12 12" stroke-linecap="butt" />\n</svg>'
        # fmt: on
    )


def test_success_icon_complete():
    template = Template(
        "{% load tablericons %}"
        + '{% icon "outline/x" size=48 class="h-4 w-4" '
        + 'data_test="a < 2" %}'
    )

    result = template.render(Context())

    assert result == (
        # fmt: off
        '<svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" data-test="a &lt; 2">\n  <path d="M18 6l-12 12" />\n  <path d="M6 6l12 12" />\n</svg>'
        # fmt: on
    )


def test_success_icon_size_none():
    template = Template("{% load tablericons %}" + '{% icon "outline/x" size=None %}')

    result = template.render(Context())

    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M18 6l-12 12" />\n  <path d="M6 6l12 12" />\n</svg>'
        # fmt: on
    )
