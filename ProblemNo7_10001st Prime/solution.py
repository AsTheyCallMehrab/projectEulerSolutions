'''
    for this problem we have to use mathematical algorithems to find the prime numbers 
    then we put them in a list and count them , and then we show the last item as 10001st prime number
    '''
count = 1
primeList = [2]
number = 2
pChecker = True

while (number < 200000) :
    for i in range(2, number):
        if number % i == 0 :
            pChecker = False
            break
    if pChecker:
        primeList.append(number)
        count += 1
    number += 1
    pChecker = True
    if count >10001:
        break
        

print(f" the 10001st prime number is : {primeList[10001]}")

'''developed by Mehrab_mahmoudifar
    difficulty level : 5%
    Thank You ♥
    '''