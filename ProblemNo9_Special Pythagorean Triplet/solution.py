"""
this problem is really easy and cool we just write the codes as 
the problem want
"""
def findTheNumber(target):
    for a in range(1,target):
        for b in range(a,target):
            c = target - a -b 
            if (a*a)+(b*b)==(c*c):
                return a,b,c
                print(a,b,c)
    return None
total = 1
num = 1000
finalNumbers = findTheNumber(num)
print("the 3 required numbers are :", finalNumbers )
for i in finalNumbers:
    total *= i
print(total)
'''developed by Mehrab_mahmoudifar
    difficulty level : 5%
    Thank You ♥
    '''