import json

staff_details =[
    {
        "Username": "Fcbah",
        "Password": "Admin",
        "Email": "fcbah1248@gmail.com",
        "Full Name": "Hephzibah Akinleye"
    },
    {
        "Username": "Noah",
        "Password": "1234",
        "Email": "akinleyenoahvalast@gmail.com",
        "Full Name": "Noah Akinleye"
    }
]

f = open("db/staff.txt", "w")
js = json.dumps(staff_details)
f.write(js)
f.close()

f = open("db/customer.txt", "w")
f.write("")
f.close()