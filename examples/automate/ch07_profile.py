import cProfile

def calcProd():
    #calculate the product of the first 100,000 numbers.
    product = 1
    for i in range (1, 100000):
        product = product * i
    return product

prod = calcProd()
print('the result is %s digits long' % len(str(prod)))
