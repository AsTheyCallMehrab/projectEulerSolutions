'''
    for this problem we need to loops starting from 999 and decrease 1 step by 1 step
    then check if it is a palindrome number or not
    '''

def palindromechecker (number):
    listnumber1=[]
    listnumber2=[]
    listnumber1=str(number)
    listnumber2=listnumber1[::-1]
    if listnumber1 == listnumber2 :
        return True
    else:
        return False

mypalindrome=[]    
for i in range(999,100,-1):
    for j in range(999,100,-1):
        state=bool
        num= i*j
        if palindromechecker(num):
            mypalindrome.append(num)

myrequirednumber=max(mypalindrome)
print("the largest palindrome made from the product of two 3-digit numbers is : ", myrequirednumber)

'''developed by Mehrab_mahmoudifar
    difficulty level : 5%
    Thank You ♥
    '''