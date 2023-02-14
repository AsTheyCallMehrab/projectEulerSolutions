'''
For This Problem First we need to Find The biggest Factor 
Then Check if it is a Prime Number or not
'''
def factors( passednumber):
    factors=[]
    d=2
    while (passednumber > 1):
        while (passednumber % d == 0):
            factors.append(d)
            passednumber /= d
        d=d+1
    return factors

largestpossibleprimefactors= factors(600851475143)
print(" Largest Prime facor of 600851475143 is : ", max(largestpossibleprimefactors)) 

'''developed by Mehrab_mahmoudifar
    difficulty level : 5%
    Thank You ♥
    '''