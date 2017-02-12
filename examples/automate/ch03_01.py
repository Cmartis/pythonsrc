def collatz(inputParam):
    if inputParam == 1:
        return inputParam
    elif (inputParam % 2 == 0):
        collatz(inputParam/2)
    elif (inputParam % 2 == 1):
        collatz(inputParam * 3 + 1)


inputParam = int(input("enter a number"))
print(collatz(inputParam))
