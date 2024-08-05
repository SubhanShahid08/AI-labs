#Comments in python
x=1
#The value of x is initialze to 1
if x>0:
    print("These are two comments") #Print a string
print("Lab1 of Artificial Intelligence") #Print a string

#input/output
txt=input("Type something to test this out:")
print(txt)

txt=input("Enter a color name of your choice: ")
print(txt)

#Multiple statements on a single line
print("Hello,world");print("My name is Subhan Shahid") #print two strings
#another example of Multiple statements on a single line
print("Give five reserve words of python:")
print("False");print("el");print("if");print("from");print("True")

#Indentation
x=1
if x>0:
 print("this statement has a single space indentation")

x=1
if x>0:
    print("this statement has a single tab indentation")  

#Numbers in python
a=1234
print(type(a))
b=-1234
print(type(b))
c=11.23
print(type(c))
d=-1.23
print(type(d))
e=2+3j
print(type(e))
f=3+4J
print(type(f))

#bool
print("Are you a web developer? If yes type Yes otherwise No..")
txt=input("Yes or No:  ")
print(txt)
if txt=="Yes" or "yes":
   x=True 
   print(x)    
   print(type(x))
else:
    x=False
    print(x)
    print(type(x))

#strings
str1="days"     #string starts and ends with double quotes
print(str1)
str2='days'     #string strats and ends single quotes
print(str2)
str3="day's"    #single quote within double quotes
print(str3)
str4='day"s'    #double quotes within single quotes
print(str4)

#special characters in string
print("This is a backslash \\ key")
print("This is a tab \t key")
print("This is a newline \n Newline key")
print("This is a backslash \'Single Quote\' key")
print("This is a backslash \"double qoute\" key")

#string indices and accessing string elements
string1="Subhan Shahid"
print(string1[0])
print(string1[-13])
print(string1[12])
print(string1[-1])
print(string1[1])
print(string1[-12])

#create a list
dryfruits_list=["almond","walnut","peanuts","pistachio"]
print(dryfruits_list[0]) #return the first element
print(dryfruits_list[0],dryfruits_list[3])  #print first and last element
print(dryfruits_list[-1])   #return last element
print(dryfruits_list[4])    #creates error

#slice list
dryfruits_list=["almond","walnut","peanuts","pistachio"]
print(dryfruits_list[0:2])  #ccuts first two items
print(dryfruits_list[1:2])  #cuts second item
print(dryfruits_list[1:-2]) #cuts second item
print(dryfruits_list[:3])   #cuts first three items
print(dryfruits_list[:])    #creates copy of original list