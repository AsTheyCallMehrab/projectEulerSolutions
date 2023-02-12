'''
    for this problem we have 3 conditions
    first of all we must create our fibonacci numbers
    then check if they are below 4 million
    then check if are they even or not
    '''

def Evencheker(n):
    if n % 2 ==0 :
        return True
    else: 
        return False


FirstNumber = 1
SecondNumber = 2
Sum = 0
TempNumber=0
while ( FirstNumber < 4000000 ) :
    TempNumber = SecondNumber
    SecondNumber += FirstNumber
    FirstNumber = TempNumber  
    if Evencheker(FirstNumber):
        Sum += FirstNumber

print(" Sum of the fibunacci Numbers Below 4 Millions Is : " , Sum)

'''developed by Mehrab_mahmoudifar
    difficulty level : 5%
    Thank You ♥
    '''