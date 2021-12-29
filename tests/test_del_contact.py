from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New", lastname="New"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts.remove(contact)
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

