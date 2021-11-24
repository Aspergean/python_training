from model.contact import Contact


def test_amend_first_contact_firstname(app):
        app.session.login(username="admin", password="secret")
        app.contact.amend_first_contact(Contact(firstname="Norm"))
        app.session.logout()

def test_amend_first_contact_lastname(app):
        app.session.login(username="admin", password="secret")
        app.contact.amend_first_contact(Contact(lastname="McDormann"))
        app.session.logout()

