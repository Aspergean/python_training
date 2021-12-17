from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
    nickname = (random_string("nickname", 15)),
    title = (random_string("title", 25)),
    company = (random_string("company", 25)),
    address = (random_string("address", 50)),
    home_phone = (random_phone(20)),
    mobile_phone = (random_phone(20)),
    work_phone = (random_phone(20)),
    fax = (random_phone(20)),
    address2 = (random_string("address2", 50)),
    phone2 = (random_phone(20)),
    notes = (random_string("notes", 100))
    for i in range(2)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
