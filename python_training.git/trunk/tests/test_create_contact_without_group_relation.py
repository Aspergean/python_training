# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact_without_group_relation(app, db, check_ui, json_contacts):
        contact = json_contacts
        old_contacts = db.get_contact_list()
#        contact = Contact(firstname="Normann", middlename="Mid", lastname="McDorm", nickname="Actor",
#                         title="StupidPlace", company="ixtrail_serenity", address="San Diego, Local str, 5",
#                          home_phone="+2343242342434", mobile_phone="+566290980893", work_phone="4577678678789",
#                          fax="34534533637", email="1@none.st", email2="hyrray@test.ry", email3="lilu@rt.by",
#                          homepage="lolali.com", birth_day="6", birth_month="November", birth_year="1989",
#                          aniv_day="13", aniv_month="June", aniv_year="2008", address2="Sydney, Last Stand av. 657",
#                          phone2="+334234324324242", notes="Stop")
        app.contact.create(contact)
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        # need to clean the results from db as " " fails the test when compare with UI
        if check_ui:
                def clean(cont):
                        return Contact(id=cont.id, firstname=' '.join(cont.first_name.split()),
                                       lastname=' '.join(cont.last_name.split()))

                ui_contacts = app.contact.get_contact_list()
                new_contacts_clean = map(clean, new_contacts)
                assert sorted(new_contacts_clean, key=Contact.id_or_max) == sorted(ui_contacts, key=Contact.id_or_max)
                print("UI was checked")

