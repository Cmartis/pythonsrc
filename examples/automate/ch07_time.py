import time
def calcProd():
    #calculate the product of the first 100,000 numbers.
    product = 1
    for i in range (1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('the result is %s digits long.' % (len(str(prod))))
print('took %s seconds to calculate.' % (endTime - startTime))
