from model.contact import Contact


def test_amend_first_contact_firstname(app):
        if app.contact.count() == 0:
                app.contact.create(Contact(firstname="test", lastname="test2"))
        old_contacts = app.contact.get_contact_list()
        app.contact.amend_first_contact(Contact(firstname="Norm"))
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) == len(new_contacts)

def test_amend_first_contact_lastname(app):
        if app.contact.count() == 0:
                app.contact.create(Contact(firstname="test1", lastname="test3"))
        old_contacts = app.contact.get_contact_list()
        app.contact.amend_first_contact(Contact(lastname="McDormann"))
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) == len(new_contacts)


