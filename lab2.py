# while loop
count = 0
while (count < 3):
    count = count + 1 
    print("Hello Geek")
# while loop
count = 1
txt=int(input("Enter a number: "))  #by default txt takes string so we have to declare the data type 
t=txt
while (count<=10):
    tab = t * count 
    print("Table of ",t,"*",count,"=",tab)
    count=count+1
    print(tab)

# Single statement while block 
count = 0
while (count == 0): print("Hello Geek")

# Iterating over a list 
print("List Iteration")
l = ["geeks", "for", "geeks"] 
for i in l:
    print(i)
# Iterating over a list 
print("List Iteration")
li=["red","blue","purple","orange","green","black"]
for i in li:
    print(i)

# Iterating over a tuple (immutable) 
print("\nTuple Iteration")
t = ("geeks", "for", "geeks") 
for i in t:
    print(i)
# Iterating over a String 
print("\nString Iteration") 
s = "Subhan Shahid"
for i in s :
 print(i)

# Iterating by index
list = ["geeks", "for", "geeks"] 
for index in range(len(list)):
 print (list[index])

print ("All letters except 'e' and 's'") 
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's': 
        continue
    print ('Current Letter :', letter)
    var = 10
# creating functions
def my_function(): 
  print("Hello from a function")
my_function() #calling function
# creating and passing parameters in functions
def table(p):
    count=1
    while (count<=10):
     tab = p * count 
     print("Table of ",p,"*",count,"=",tab)
     count=count+1
txt=int(input("Enter a Number:"))
table(txt)

my_function(10,4)
def printfun(country="PAKISTAN"): #Pakistan is default parameter
    print(country)

printfun()  #When called without parameter default parameter is used
printfun("Palestine")  # Default Parameter can be changed by passing a parameter

def listfun(myList):
    for i in myList:
        print(i)
        
    listfun(myList)
def returnfun(a,b):
    return a*b

a=int(input("Enter num 1: "))
b=int(input("Enter num 2: "))
print(returnfun(a,b)) #return function returns the value of the function
print(f"{a} * {b} = {returnfun(a,b)}") #format using f and placeholders{}

#CLasses
print("Classes ")
class myclass:
    x=5

obj1=myclass
print(obj1.x)

#The above class is just a simple class syntax
##init functions
class Cars:
    def __init__(self,brand,model,color): # self parameter represents the instance of object created
        self.brand=brand
        self.model=model
        self.color=color
    def display(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nColor {self.color}")
        

obj1=Cars("Toyota","2023","Black")
obj1.display()
    