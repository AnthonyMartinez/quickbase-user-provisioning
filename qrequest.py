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
            'usertext': 'Hey x,\n\n\nWelcome to the Community Outreach Group! This email is\
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



