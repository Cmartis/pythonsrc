birthdays = {'rachel':'26th Sept 2006', 'ryan':'9th Jan 2003', 'chris':'28th Jan 1973', 'medha':'8th Sep 1973', 'rita':'14th July 1940'}

while True:
    print('enter a name: (blank to quit]')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print(' i do not have the birthday for ' + name)
        print('what is their birthday')
        bday = input()
        birthdays[name] = bday
        print('birthdays database updated')
              
