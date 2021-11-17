# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact_without_group_relation(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="Normann", lastname="McDorm", address="San Diego, Local str, 5", home="+2343242342434",
                    email="1@none.st"))
        app.session.logout()
