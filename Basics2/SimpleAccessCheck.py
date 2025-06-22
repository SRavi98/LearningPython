name = input('Enter your name: ')
if name == 'Ravi':
    print(f'Welcome {name}')
    password = input('Enter your password: ')

    if password == 'ravi@98':
        print('Access Granted')
    else:
        print('Wrong Password!. Access Denied!')
elif name == 'Shiva':
    brother = input("Are you ravi's brother?(yes/no): ")
    if brother == 'yes':
        print('Access Granted!')
        password = input("Enter admin's password: ")
        if password == 'ravi@98':
            print('Access Granted')
        else:
            print('Wrong Password!. Access Denied!')
    else:
        print("Access Denied!")
else:
    print('Access Denied!. Require Admin Access!') 