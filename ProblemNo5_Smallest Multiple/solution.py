'''
    for this problem we need to factorize number 1-20 and then count the maximum factor of prime numbers
    then if we multiply them , we reach the smallet number that can be divide by numbers between 1-20.
    we have these factors:
    2^4
    3^2
    5^1
    7^1
    11^1
    13^1
    17^1
    19^1
    '''
factors = [ 16, 9, 5, 7, 11, 13, 17, 19 ]
number = 1
for i in factors:
    number *= i

print(f"the result number is : {number}")

'''developed by Mehrab_mahmoudifar
    difficulty level : 5%
    Thank You ♥
    '''