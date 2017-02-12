#this program calculates the count of characters for a given string
import pprint

message = 'This message does not have man repetiting characters,'\
            'unlike other messages that have repetiting characters'
count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

pprint.pprint(count)

                    
