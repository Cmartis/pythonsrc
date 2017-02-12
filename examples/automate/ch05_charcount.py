#this program calculates the count of characters for a given string

message = 'This message does not have man repetiting characters,'\
            'unlike other messages that have repetiting characters'
count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

for item in count.items():
    print(item)

                    
