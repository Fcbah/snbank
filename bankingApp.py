import json
import random
import os

def displayLoginMenu():
    output = ""
    output += "<1> Staff Login \n"
    output += "<2> Close App \n"
    print(output)

def displayStaffMenu():
    output = ""
    output += "<1> Create New Bank Account \n"
    output += "<2> Check Account Details \n"
    output += "<3> Logout \n"
    print(output)

def findStaff(Username, Password):
    try:
        f = open("db/staff.txt", 'r')
    except OSError:
        import initialize
        f = open("db/staff.txt", 'r')

    staffs = json.loads(f.read())
    f.close()

    for staff in staffs:
        if(staff['Username'].lower() == Username.lower() and staff['Password'] == Password):
            return staff
            
    return None

def findAccount(accountNumber):
    f = open("db/customer.txt", 'r')
    accounts = json.loads(f.read())
    f.close()

    if accounts:
        for account in accounts:
            if account["Account Number"] == accountNumber:
                return account
        return False
    return None

def generateAccountNumber():
    unique = False
    accountNumber = ""
    while not unique:
        accountNumber = ""
        for x in range(10):
            accountNumber += str(random.randint(1,9))
        if not findAccount(accountNumber):
            unique = True

    return accountNumber


def createAccount(accountName, openingBalance, accountType, accountEmail):
    accountNumber = generateAccountNumber()
    
    account = {
        "Account name": accountName,
        "Opening Balance": openingBalance,
        "Account Type": accountType,
        "Account email": accountEmail,
        "Account Number": accountNumber
        }
    
    f = open("db/customer.txt", 'r')
    raw = f.read()
    accountList = json.loads(raw)
    f.close()

    if not raw:
        accountlist = []

    accountList.append(account)
    
    f = open("db/customer.txt", 'w')
    f.write(json.dumps(accountList)) 
    f.close()

    return accountNumber

def create_session(username):
    f = open("db/session.json", 'w')
    f.write(json.dumps({"Username":username})) 
    f.close()

def destroy_session():
    try:
        os.remove("db/session.json")
    except:
        pass

def find_current_session():
    try:
        f = open("db/session.json", 'r')
        username = json.loads(f.read())
        f.close()
        
        f = open("db/staff.txt", 'r')
        staffs = json.loads(f.read())
        f.close()

        for staff in staffs:
            if(staff['Username'].lower() == username.lower()):
                return staff
        
        destroy_session() #If the staff does not exist then the session should be destroyed
        return False
        
    except OSError:
        return None
    

if "__name__" == "__main__":
    while True:
        session = find_current_session()
        if(session):
            displayStaffMenu()

            possible = ['1','2','3']
            response = input("Enter Your Choice: ")
            if response in possible:
                if response == '1':
                    print("To create a new Account, enter the following details: ")
                    details = ["Account name","Opening Balance","Account Type","Account email"]
                    response =[]
                    for info in details:
                        response.append(input("%s: "%info))
                    accountNumber = createAccount(response[0],response[1],response[2],response[3])
                    print("------------------------------")
                    print("The account number for '%s' is: %s"%(response[0],accountNumber))
                elif response == '2':
                    accountNumber = input("Enter the account number for the account: ")
                    account = findAccount(accountNumber)
                    if account:
                        print("\nAccount details for %s"%accountNumber)
                        print("----------------------- ")
                        for key in account:
                            print("%s \t:%s"%(key,account[key]))
                    else:
                        print("Wrong Account Number: Account is not registered with us")
                else:
                    destroy_session()
            else:
                print("Invalid input, valid inputs are only --> %s "%", ".join(possible))

        else:
            displayLoginMenu()

            possible = ['1','2']
            response = input("Enter Your Choice: ")
            if response in possible:
                if response == "1":
                    username = input("Enter your Username: ")
                    password = input("Enter your password: ")
                    staff = findStaff(username,password)
                    if not staff:
                        print("Invalid Username and/or Password")
                    else:
                        create_session(username)
                        print("Welcome %s, you have logged in successfully"%staff["Full Name"])
                elif response == "2":
                    break            
            else:
                print("Invalid input, valid inputs are only --> %s "%", ".join(possible))