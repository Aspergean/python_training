from model.contact import Contact


def test_amend_first_contact_firstname(app):
        app.contact.amend_first_contact(Contact(firstname="Norm"))

def test_amend_first_contact_lastname(app):
        app.contact.amend_first_contact(Contact(lastname="McDormann"))


