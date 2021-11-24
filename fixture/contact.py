from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def return_to_home_page(self):
        wd = self.app.wd
        # return to home page
        wd.find_element_by_link_text("home page").click()


    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact info
        self.fill_contact_form(contact)
        # submit form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_dropdown_value("bday", contact.birth_day)
        self.change_dropdown_value("bmonth", contact.birth_month)
        self.change_field_value("byear", contact.birth_year)
        self.change_dropdown_value("aday", contact.aniv_day)
        self.change_dropdown_value("amonth", contact.aniv_month)
        self.change_field_value("ayear", contact.aniv_year)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_dropdown_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)
            wd.find_element_by_css_selector(
                "select[name=" + str(field_name) + "] > option[value='" + str(value) + "']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        # open home page
        self.open_home_page()
        self.select_first_contact()
        # click delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to.alert.accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def amend_first_contact(self, contact):
        wd = self.app.wd
        # open home page
        self.open_home_page()
        # edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact info
        self.fill_contact_form(contact)
        # submit amendments
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def open_home_page(self):
        wd = self.app.wd
        # open home page
        wd.find_element_by_link_text("home").click()
