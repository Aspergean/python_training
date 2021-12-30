import re
from model.contact import Contact
from random import randrange


def test_contacts_info_ui_vs_db(app, db):
    home_contacts_list = app.contact.get_contact_list()
    db_contact_list = db.get_contact_list()
    db_contacts_clean = map(clean, db_contact_list)
    assert sorted(home_contacts_list, key=Contact.id_or_max) == sorted(db_contacts_clean, key=Contact.id_or_max)

def test_contact_info_on_home_page(app):
    home_contacts_list = app.contact.get_contact_list()
    index = randrange(len(home_contacts_list))
    contact_from_home_page = home_contacts_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.id == contact_from_edit_page.id
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert clear(contact_from_view_page.all_phones) == merge_phones_like_on_home_page(contact_from_edit_page)
    #assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    #assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    #assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(s):
    return re.sub("[/() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone,  contact.mobile_phone,
                                        contact.work_phone, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != '',
               filter(lambda x: x is not None, [contact.email,  contact.email2, contact.email3])))


def clean(contact):
    firstname = ' '.join(contact.firstname.split())
    lastname = ' '.join(contact.lastname.split())
    address = contact.address
    all_phones_from_home_page = merge_phones_like_on_home_page(contact)
    all_emails_from_home_page = merge_emails_like_on_home_page(contact)
    print(firstname, lastname, address, all_phones_from_home_page, all_emails_from_home_page)
    return Contact(id=contact.id, firstname=firstname, lastname=lastname, address=address,
                   all_phones_from_home_page=all_phones_from_home_page, all_emails_from_home_page=all_emails_from_home_page)


