from model.contact import Contact


def test_amend_first_contact_firstname(app):
        if app.contact.count() == 0:
                app.contact.create(Contact(firstname="test", lastname="test2"))
        app.contact.amend_first_contact(Contact(firstname="Norm"))

def test_amend_first_contact_lastname(app):
        if app.contact.count() == 0:
                app.contact.create(Contact(firstname="test1", lastname="test3"))
        app.contact.amend_first_contact(Contact(lastname="McDormann"))


