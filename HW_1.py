import re

try:
    name = input('Enter your name : ')
    while name:
        if re.findall('[A-z]', name):
            email = input('Enter your Email : ')
            while email:
                if re.findall('^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$', email):
                    print("Valid Email")
                    url = input('Enter Your URL : ')
                    while url:
                        if re.findall('((https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+))', url):
                            print(f"valid Data")
                            print(f'Your name : {name}')
                            print(f'Your email :{email}')
                            print(f'Your URL : {url}')
                            break
                    break


                else:
                   print("InValid Email")
                   email = input('Enter your Email : ')
            break
        else:
            print("InValid name")
            name = input('Enter your name : ')


except Exception as ex:
    print("Invalid Data", ex)
    pass 