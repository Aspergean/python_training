# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    s = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    clear_string = ' '.join([t for t in s.split(' ') if t])  # delete all unnecessary additional spaces
    return clear_string

def random_phone(maxlen):
    dividers = " +-()"
    symbols = dividers + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(email="1@none.st", email2="hyrray@test.ry", email3="lilu@rt.by",
            homepage="lolali.com", birth_day="6", birth_month="November", birth_year="1989",
            aniv_day="13", aniv_month="June", aniv_year="2008",
    firstname = (random_string("firstname", 15)),
    middlename = (random_string("middlename", 20)),
    lastname = (random_string("lastname", 20)),
    nickname = ("", random_string("nickname", 15)),
    title = ("", random_string("title", 25)),
    company = ("", random_string("company", 25)),
    address = ("", random_string("address", 50)),
    home_phone = ("", random_phone(20)),
    mobile_phone = ("", random_phone(20)),
    work_phone = ("", random_phone(20)),
    fax = ("", random_phone(20)),
    address2 = ("", random_string("address2", 50)),
    phone2 = ("", random_phone(20)),
    notes = ("", random_string("notes", 100)))
    for i in range(2)
           ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_create_contact_without_group_relation(app, contact):
        old_contacts = app.contact.get_contact_list()
#        contact = Contact(firstname="Normann", middlename="Mid", lastname="McDorm", nickname="Actor",
#                         title="StupidPlace", company="ixtrail_serenity", address="San Diego, Local str, 5",
#                          home_phone="+2343242342434", mobile_phone="+566290980893", work_phone="4577678678789",
#                          fax="34534533637", email="1@none.st", email2="hyrray@test.ry", email3="lilu@rt.by",
#                          homepage="lolali.com", birth_day="6", birth_month="November", birth_year="1989",
#                          aniv_day="13", aniv_month="June", aniv_year="2008", address2="Sydney, Last Stand av. 657",
#                          phone2="+334234324324242", notes="Stop")
        app.contact.create(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

