from __future__ import annotations

from xml.etree import ElementTree

import pytest

import tablericons


def test_load_icon_success_outline():
    svg = tablericons._load_icon("outline/x")
    assert isinstance(svg, ElementTree.Element)
    assert svg.tag == ElementTree.QName("svg")


def test_load_icon_success_solid():
    svg = tablericons._load_icon("outline/x")
    assert isinstance(svg, ElementTree.Element)
    assert svg.tag == ElementTree.QName("svg")


def test_load_icon_success_mini():
    svg = tablericons._load_icon("outline/x")
    assert isinstance(svg, ElementTree.Element)
    assert svg.tag == ElementTree.QName("svg")


def test_load_icon_fail_unknown():
    with pytest.raises(tablericons.IconDoesNotExist) as excinfo:
        tablericons._load_icon("hoome")

    assert excinfo.value.args == ("The icon 'hoome' does not exist.",)
