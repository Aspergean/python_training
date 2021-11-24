from model.contact import Contact


def test_amend_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.amend_first_contact(
        Contact(firstname="Norm", middlename="Mid_Mid", lastname="McDormann", nickname="Actor",
                title="StupidPlace", company="ixtrail_serenity", address="San Diego, Local str, 5",
                home="+567756575686568", mobile="+566290980893",
                work_phone="4577678678789", fax="34534533637", email="1@none.st", email2="hyrray666666@test.ry",
                email3="lilu@rt.by",
                homepage="lolali.com", birth_day="6", birth_month="November", birth_year="1989", aniv_day="13",
                aniv_month="June", aniv_year="2008",
                address2="Sydney, Last Stand av. 657", phone2="+334234324324242", notes="Stop"))
    app.session.logout()
