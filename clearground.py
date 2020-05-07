#Sorry this is a private script
#just to ensure that the customer.txt is empty after doing all my tests

import os

f = open("db/customer.txt", "w")
f.write("")
f.close()

try:
    os.remove("db/session.json")
except:
    pass

try:
    os.remove("db/staff.txt")
except:
    pass

import initialize