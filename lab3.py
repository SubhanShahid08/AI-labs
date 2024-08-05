#Question1
print("NUMBERS DIVISBLE BY BOTH 5 AND 7 ARE: ")
for i in range(1500,2700):
    if i%7==0 and i%5==0:
        print(i,end=',')

#Question2
temp=int(input("Enter temperature in celsius: "))
f=((temp * 9/5)+32)
print("Temperature in Farheniet: ",f)
temp=int(input("Enter temperature in Farheniet: "))
f=(temp - 32)*(5/9)
print("Temperature in celsius",f)

#Question3
import random
num=random.randint(1,9)
print(num)
while(True):
    guess=int(input("Enter your guess:"))
    if guess==num:
        print("Well Guessed")
        break

#Question4
"""
*
**
***
****
*****
****
***
**

"""
for i in range(6):
    for j in range(i):
        print("*",end="")
    print("")

for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print("")

#Question5
word=input("Enter a word: ")
a=len(word)-1
rev=""
for i in range(len(word)):
    rev=rev+word[a]
    a=a-1
print("Reversed word is:",rev)
print("Another method to reverse a word is word[::-1]")
rev2=word[::-1]
print(rev2)

#Question6
numbers=[1,2,3,4,5,6,7,8,9]
odd=0
even=0
for x in numbers:
    if x%2==0:
        even+=1
    else:
        odd+=1
print("Even: ",even)
print("Odd: ",odd)

#Question7
datalist=[1452,11.23,1+2j,True,'W3resource',(0,-1),[5,12],{"class":'V',"Section":'A' }]
for i in datalist:
    print(type(i))

#Question8
for i in range(0,6):
    if i==3 or i==6:
        continue
    print(i)

#Question9
list1=[0,1]
i=1
while(True):
    print(i)
    num= list1[i]+list1[i-1]
    if(num>50):
        break
    list1.append(num)
    i+=1
print(list1)

#Question10
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("Fizzbuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
        
#Question11
rows=int(input("Enter number of rows: "))
col=int(input("Enter number of Coloumns: "))
array_2d = [[0 for _ in range(col)] for _ in range(rows)]
# list1=[[rows][col]]
for i in range(rows):
    for j in range(col):
        array_2d[i][j]=i*j
print(array_2d)

#Question12
list1=[]

while(True):
    txt=input("Enter nothing to terminate\nEnter String:")
    if txt=="":
            break
    else:
        list1.append(txt.lower())
print(list1)

#Question13
list1=[]
while(True):
   binary_num= input("Enter 4 digits Binary number: (Enter -1 to break)")
   if(binary_num=="-1"):
       break
   decimal_num=int(binary_num,2)
   if decimal_num%5==0:
       list1.append(binary_num)
print(list1)

#Question14
txt=input("Enter string: ")
Letters=0
Digits=0
for i in range(len(txt)):
    if txt[i].isalpha():
        Letters+=1
    elif txt[i].isnumeric():
        Digits+=1
print("Letters: ",Letters)
print("Digits: ",Digits)

#Question15
password=input("Enter password: ")
i=0
alphacount=0
numericcount=0
charcount=0
if len(password) >= 6 and len(password) <= 16:
    while i < len(password):
        if alphacount == 0 and password[i].isalpha():
            alphacount += 1
        if numericcount == 0 and password[i].isdigit():
            numericcount += 1
        if charcount == 0 and (password[i] == '$' or password[i] == '#' or password[i] == '@'):
            charcount += 1
        i += 1
    else:
        if alphacount > 0 and numericcount > 0 and charcount > 0:
            print("Password is valid")
        else:
            print("Password must contain at least one alphabet, one numeric digit, and one special character ($, #, @)")
else:
    print("Password length should be between 6 and 15 characters")


