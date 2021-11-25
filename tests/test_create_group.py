# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Test", header="New Group1", footer="New Group1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

