
from sys import maxsize

class Contact:

    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None, email=None, email2=None,
                 email3=None, homepage=None, birth_day=None, birth_month=None, birth_year=None, aniv_day=None,
                 aniv_month=None, aniv_year=None, address2=None, phone2=None, notes=None,
                 all_in_all_phones=None, all_in_all_emails=None, all_phones=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.aniv_day = aniv_day
        self.aniv_month = aniv_month
        self.aniv_year = aniv_year
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_in_all_phones = all_in_all_phones
        self.all_in_all_emails = all_in_all_emails
        self.all_phones = all_phones

    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.id, self.firstname, self.lastname, self.address,
                                           self.all_in_all_phones, self.all_in_all_emails)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.firstname is None or other.firstname is None or self.firstname == other.firstname) and \
               (self.lastname is None or other.lastname is None or self.lastname == other.lastname) and \
               (self.address is None or other.address is None or self.address == other.address) and \
               (self.all_in_all_phones is None or other.all_in_all_phones is None
                or self.all_in_all_phones == other.all_in_all_phones) and \
               (self.all_in_all_emails is None or other.all_in_all_emails is None
                or self.all_in_all_emails == other.all_in_all_emails)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
