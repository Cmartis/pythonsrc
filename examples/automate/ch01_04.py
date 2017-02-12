while True:
    print('who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('hello, joe. what is your password ?(it is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('access granted.')
