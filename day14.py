'''12,
Tokens,Datatypes --> Control Flow Statements --> if.elif,else,for,while,break,continue..
Procedure Oriented programming

Funtions --> A function is ablock  of code which performs a specific task
Its a reusable group of statements where we dwfine using
def keyword
Advantages --> Code reusability,code maintainability,ease of debuggin,
Avoiding code duplication,modularity

def fname(parameters): Function defn
    """ Doc String"""  Description
    statement(s).....
    ..........         Function body
    return value(s)......
fname(args)
'''
'''
#To Perform sum of given objects
def add(a,b):
    """Sum of objects"""
    c = a+b
    return c
print(add(12,3)) #Addition
print(add('code','gnan')) #concatenation
print(add([12,5],[12,34])) #Merging
c,d = map(int,input("Enter the values:").split(','))
print(c,d)
print(add(c,d))

def add(a,b):
    """sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12,-34)) #it returns result along with None
'''
'''
name,age,salary = "manasa",21,500000
#usage of return
def details():
    #return name,age,salary
    #retyrn "Codegnana"
    #return 23+34+45
    return #it returns None as output
print(details())

There are 5 types of arguments:
--> positional Arguments
--> keyword arguments
--> defalult arguments
-->variable length arguments (*args)
--> keyword variable length arguments (**kwargs)
'''
'''
#Positional Arguments -->Number of arguments in function defn should
#match with function call (order has to be maintained)
#print(len(123,234)) this is as per built-in len(obj) will accept one arguments

def details(name,place):
    """To store the details"""
    #name = "codegnan"
    #place = "Hyderabad"
    return name,place
#print(details("manasa","codegnan"))
#print(details("sai","vizag"))
#print(details("wanaparthy","pandu",4)) #raises TypeError as only 2 arguments to 
c,d = map(str,input("Enter the values").split(','))
details(c,d)
'''
'''
#Default arguments --> we can make arguments as default but not first argument
#as default
def grocery (item="Burger", price): #non default always follows default
    """usage of default arguments"""
    print(f'The Item is {item} and price is{price}')
grocery("milk",32)
#grocery(32,"milk")
grocery("Bread") #by defalut we have given price as 35
grocery() #as both item and price as default arguments
'''

#keyword arguments -->Whenver we want to specify the name of argument
def employee(name,salary,role):
    """Keyword arguments usage"""
    print(f'Employee Name is {name}, role is {role} and salary is {salary},\
      works in {place}')
employee("Manasa",20000,"Admin")
employee(salary = 25000, role="Frontdesk",name = "Ashu")
employee("manasa",25000,"IT","Amazon")


































