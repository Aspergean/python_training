# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact_without_group_relation(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="Normann", lastname="McDorm", address="San Diego, Local str, 5", home="+2343242342434", email="1@none.st"))
        app.logout()
