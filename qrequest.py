import requests

# all the relevant info
url = 'https://communityoutreachgroup.quickbase.com'

db = '/db/'
db_payroll = url + db + 'bjjnqusjp'

username = 'anthonymartinez'
password = '' # insert password


# for provisioning
email = ''
roleID = ''
fname = ''
lname = ''
ticket = ''
apptoken = ''
userid = ''


def provision():
    data = {
            'a': 'API_ProvisionUser',
            'email': email,
            'roleID': roleID,
            'fname': fname,
            'lname': lname,
            'ticket': ticket,
            'apptoken': apptoken
            }

    r = requests.post(db_payroll, params=data)

    print(r.text)

def invite():
    data = {
            'a': 'API_SendInvitation',
            'userid': '',
            'ticket': ticket,
            'apptoken': apptoken,
            'usertext': 'Hey ' + fname + ' ,\n\n\nWelcome to the Community Outreach Group! This email is\
                    to invite you to create a log in for Quickbase, our online platform\
                    where you\'ll be able to log expenses, record your time, and other\
                    important HR tasks. The link to set your password and other info should\
                    be included below. If it does not, or you have any other trouble\
                    gaining access, please email me any time at anthony.\
                    martinez@communityoutreachgroup.net\n\nSincerely,\nAnthony Martinez\
                    Data & Technology Director\nCommunity Outreach Group'
            }
    
    r = requests.post(db_payroll, params=data)
    print(r.text)




# parameters
def authenticate():
    data = {
            'a': 'API_Authenticate',
            'username': username,
            'password': password
            }

    r = requests.post(url, params=data)

    print(r.text)

def logout():
    data = {
            'a': 'API_SignOut'
            }
    r = requests.post(url, params=data)

    print(r.text)


def params_login():
    global username
    global password

    print("enter username...")
    username = raw_input()
    print("enter password...")
    password = raw_input()
       
def params_provision():
    print("provisioning user...\nenter email")
    global email
    global roleID
    global fname
    global lname

    email = raw_input()
    print("enter the role ID")
    roleID = raw_input()
    print("enter first name")
    fname = raw_input()
    print("enter last name")
    lname = raw_input()


if __name__ == "__main__":
    params_login()
    print("enter \"provision\" to begin provisioning process, \"invite\" to begin invitation\
            process, and \"login\" to login. enter \"quit\" to quit.")
    choice = raw_input()

    while choice != "quit":
        if choice == "provision":
            params_provision()
                
        if choice == "invite":
            #params_invite()
            pass 
        if choice == "login":
            print("working...")
            authenticate()
        if choice == "logout":
            logout()

        print("enter \"provision\" to begin provisioning process, \"invite\" to begin invitation\
                process, and \"login\" to login. enter \"quit\" to quit.")
        choice = raw_input()




