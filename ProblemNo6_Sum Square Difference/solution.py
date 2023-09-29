'''
    this problem got an easy solution , just do the math
    '''
sumOfSqures = 0
squareOfSums = 0
for i in range(1,101):
    sumOfSqures += i*i
    i+=1

for j in range(1,101):
    squareOfSums += j
    j+=1
squareOfSums = squareOfSums*squareOfSums

print(f"the difference between the square of sums  and sums of squares is : {squareOfSums - sumOfSqures }")

'''developed by Mehrab_mahmoudifar
    difficulty level : 5%
    Thank You ♥
    '''