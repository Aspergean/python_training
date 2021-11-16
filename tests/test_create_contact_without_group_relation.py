# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact_without_group_relation(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="Normann", lastname="McDorm", address="San Diego, Local str, 5", home="+2343242342434",
                    email="1@none.st"))
        app.session.logout()
