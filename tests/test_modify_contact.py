import pytest
from model.contact import Contact
import random


def test_amend_first_contact_firstname(app, db, check_ui, json_contacts):
    contact = json_contacts
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New", lastname="New"))
    old_contacts = db.get_contact_list()
    choose_contact = random.choice(old_contacts)
    contact.id = choose_contact.id
    app.contact.modify_contact_by_id(contact)
    new_contacts = db.get_contact_list()
    index = old_contacts.index(choose_contact)
    old_contacts[index] = contact
    assert old_contacts == new_contacts
    # need to clean the results from db as " " fails the test when compare with UI
    if check_ui:
        def clean(cont):
            return Contact(id=cont.id, firstname=' '.join(cont.firstname.split()),
                           lastname=' '.join(cont.lastname.split()))

        ui_contacts = app.contact.get_contact_list()
        new_contacts_clean = map(clean, new_contacts)
        assert sorted(new_contacts_clean, key=Contact.id_or_max) == sorted(ui_contacts, key=Contact.id_or_max)
        print("UI was checked")

        #def test_amend_first_contact_lastname(app):
        #        if app.contact.count() == 0:
        #                app.contact.create(Contact(firstname="test1", lastname="test3"))
        #        old_contacts = app.contact.get_contact_list()
        #        index = randrange(len(old_contacts))
        #        contact = Contact(lastname="McDormann")
        #        contact.id = old_contacts[index].id
        #        app.contact.modify_contact_by_index(index, contact)
        #        new_contacts = app.contact.get_contact_list()
        #        assert len(old_contacts) == len(new_contacts)
        #        old_contacts[index] = contact
        #        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


