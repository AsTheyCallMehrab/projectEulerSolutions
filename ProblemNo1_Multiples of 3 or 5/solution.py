''' For This question we need a function , That check if our number is a multiples
3 or 5 for then return it and if our condition was True , sum it up !'''

def multiples3_5(n):
    if ( n % 3 == 0 or n % 5 == 0):
        return True
    else:
        return False

sum =0
for i in range(1,1000):
    if multiples3_5(i):
        sum +=i

print (" sum of mulpiples of 3 or 5 under 1000 is : ", sum)

'''developed by Mehrab_mahmoudifar
    difficulty level : 5%
    Thank You ♥
    '''
