from model.contact import Contact

def test_delete_first_group(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test1", lastname="test2"))
    app.contact.delete_first_contact()
