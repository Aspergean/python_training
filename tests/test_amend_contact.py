from model.contact import Contact


def test_amend_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.amend_first_contact(
        Contact(firstname="Norman", lastname="McDormtheOldest", address="San Diego, Local str, 5", home="+2343969696969",
                    email="1@none.st"))
    app.session.logout()