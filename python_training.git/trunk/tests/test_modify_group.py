from model.group import Group
import random


def test_modify_group_name(app, db, check_ui, json_groups):
    group = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Created'))
    old_groups = db.get_group_list()
    choose_group = random.choice(old_groups)
    group.id = choose_group.id
    app.group.modify_group_by_id(group)
    new_groups = db.get_group_list()
    index = old_groups.index(choose_group)
    old_groups[index] = group       # change amended group to new group in the old_list
    assert old_groups == new_groups     # compare
    # need to clean the results from db as " " fails the test when compare with UI
    if check_ui:
        def clean(gr):
            return Group(id=gr.id, name=gr.name.strip())
        ui_groups = app.group.get_group_list()
        new_groups_clean = map(clean, new_groups)
        assert sorted(new_groups_clean, key=Group.id_or_max) == sorted(ui_groups, key=Group.id_or_max)
        print("UI was checked")


    #def test_modify_group_header(app):
    #    if app.group.count() == 0:
    #        app.group.create(Group(name="test1"))
    #    old_groups = app.group.get_group_list()
    #    index = randrange(len(old_groups))
    #    group = Group(header="New Header")
    #    group.id = old_groups[index].id
    #    app.group.modify_group_by_index(index, group)
    #    new_groups = app.group.get_group_list()
    #    assert len(old_groups) == len(new_groups)
    #    old_groups[index] = group
    #    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)