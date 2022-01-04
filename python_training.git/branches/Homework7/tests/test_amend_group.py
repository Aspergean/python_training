from model.group import Group


def test_amend_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.amend_first_group(
        Group(name="Amended", header="Old Group1", footer="Old Group1"))
    app.session.logout()
