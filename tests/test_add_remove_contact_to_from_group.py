import random

from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group

orm = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

def test_add_contact_to_group(app):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name='newGroup'))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact(firstname="NewFirstname", lastname="NewLastname"))
    contact = random.choice(orm.get_contacts_not_in_group(group))
    contacts_in_group_before = list(orm.get_contacts_in_group(group))
    app.contact.add_contact_to_group(contact.id, group)
    contacts_in_group_after = list(orm.get_contacts_in_group(group))
    contacts_in_group_before.append(contact)
    assert sorted(contacts_in_group_before, key=Contact.id_or_max) == sorted(contacts_in_group_after, key=Contact.id_or_max)

def test_delete_contact_from_group(app):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name='newGroup'))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_in_group(group)) == 0:
        app.contact.create(Contact(firstname="NewFirstname", lastname="NewLastname"))
        contact = orm.get_contacts_not_in_group(group)[0]
        app.contact.add_contact_to_group(contact.id, group)
    else:
        contact = random.choice(orm.get_contacts_in_group(group))
    contacts_in_group_before = list(orm.get_contacts_in_group(group))
    app.contact.remove_contact_from_group(contact.id, group)
    contacts_in_group_after = list(orm.get_contacts_in_group(group))
    contacts_in_group_before.remove(contact)
    assert sorted(contacts_in_group_before, key=Contact.id_or_max) == sorted(contacts_in_group_after, key=Contact.id_or_max)
