from model.contact import Contact

def test_delete_first_group(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test1", lastname="test2"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
