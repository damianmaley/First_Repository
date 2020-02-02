username = 'Damian'
for tries in reversed(range(3)):
    user = input('Enter your user name>>> ')
    user = user.title()
    if user == username:
        break
    else:
        print(f'Wrong input... you have {tries} trials left')
else: 
    raise SystemExit('Ran out of tries.. Login after 15 minutes')
print(f'Welcome to the portal {user}')
