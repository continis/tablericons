from __future__ import annotations

from typing import Any

import django
from django.conf import settings
from django.template import Context, Template

settings.configure(
    ROOT_URLCONF=__name__,  # Make this module the urlconf
    SECRET_KEY="insecure",
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "APP_DIRS": False,
        },
    ],
    INSTALLED_APPS=["lucide"],
)
urlpatterns: list[Any] = []
django.setup()


def test_success_icon():
    template = Template('{% load lucide %}{% lucide "x" %}')

    result = template.render(Context())
    print(result)
    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M18 6 6 18" />\n  <path d="m6 6 12 12" />\n</svg>'
        # fmt: on
    )


def test_success_icon_path_attr():
    template = Template(
        "{% load lucide %}" + '{% lucide "x" stroke_linecap="butt" %}'
    )

    result = template.render(Context())

    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M18 6 6 18" stroke-linecap="butt" />\n  <path d="m6 6 12 12" stroke-linecap="butt" />\n</svg>'
        # fmt: on
    )


def test_success_icon_complete():
    template = Template(
        "{% load lucide %}"
        + '{% lucide "x" size=48 class="h-4 w-4" '
        + 'data_test="a < 2" %}'
    )

    result = template.render(Context())

    assert result == (
        # fmt: off
        '<svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" data-test="a &lt; 2">\n  <path d="M18 6 6 18" />\n  <path d="m6 6 12 12" />\n</svg>'
        # fmt: on
    )


def test_success_icon_size_none():
    template = Template("{% load lucide %}" + '{% lucide "x" size=None %}')

    result = template.render(Context())

    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M18 6 6 18" />\n  <path d="m6 6 12 12" />\n</svg>'
        # fmt: on
    )
