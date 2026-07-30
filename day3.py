#Numeric datatype -->int,float,complex along with boolean
#Input formating  -->Accepting input from the user --> input()
#Accepting integer input from user
#by default input() accepts any input --> str
#int(input()) -->will accept only integers
'''age = float(input('Enter the age:'))
print(age)
print(type(age))

#float(input()) -->accepts integer,float values
age = float9input("Enter the age:"))
print(age)
print(type(age))'''
'''
#Accpeting string input from user
name = input("Enter the names")
print(name)
print(type(name))
'''

'''
#Accepting group of values
marks = int(input("Enter the marks:"))
print(marks)'''
'''
a = input().split() #by default split() has space
print(a)
a = input().split() #now you enter spaces in output
print(a)
#comma separated values
a = input("Enter the values:").split('&')
print(a)

#List of integers
marks = list(map(int,input("Enter the values").split(',')))
print(marks)            
'''
'''
#now we want to accept 2 values from user
age,salary = map(int,input("Enter the values").split(','))
print(age)
print(salary)
'''
'''
#single input --> int(input())
#two inputs -->a,b  = map(int,input().split(',')
# any number result as list --> a = list(map(int,input().split(',')))
age,salary = map(float,input("Enter the values").split(','))
print(age)
print(salary)
'''
'''
age,salary = listmap((float,input("Enter the values").split(',')))
print(age)
print(salary)
'''
'''
#Accepting input from user -->int,float -> input formating

#Operators -->Operators perform operations between values (operands)
#7 types -->Arithmetic,Assignment,Comparison (Relationship)
#Membership,Identity,Logical,Bitwise

#Arithmetic Operators -->Arithmetic operations
#+, -,*,/
print(5+3)
print(5-3)
print(5*3)
print(5/3)
'''
'''
#Float  value
#Floor Division (Integer division)  -->returns quotient
print(5//3)
print(5%3)
#modulus --.division rules -->returns  remainder
print(5%3)

print(5**3)
'''
'''
#Task -->Accept integer input as length,breadth --. fing the area of rectangle
#Area = length * breadth
length = int(input("enter the length"))
breadth = int(input("enter the breadth"))
print(length)
print(breadth)
print(length*breadth)
'''
'''
length = map()int(input("enter the length"))
breadth = map()int(input("enter the breadth"))
print(length)
print(breadth)
'''

#Assignment operators -->assign the values
# =,+=, -=
a = 45
print(a)
#update the value of a
a = a + 5 #a+= 5
print(a)

b = 35
b += a
print(b)

c = 20
c -= a
print(c)

#Task : *=, /=, //=, %=, **= workout
b = 35
b *= 2
print(b)


c = 20
c /= 4
print(c)

d = 40
d //= 10
print(d)

e = 30
e %= 5
print(e)

f = 50
f **= 5
print(f)


a = 40
print(a)
#Update the value of a
b *=a 
print (b)
'''
#Comaprison Operators --. we compare the values --.boolean
# ==(equal to) , != (not equalto) , < (lessthan) , < (greater than)
# <= ( less than or equal to) >= (greater than or equal to)

age = 25
print(age == 25)
print(age != 25)
print(age < 25)
print(age <=25)
print(age > 35)
print(age >= 35)

print(-5 < -1)
print(-5 > -1)

#Membership Operators --> in, not in --.boolean
#it checks for the existance of an object in a collection

marks = [156,75,45,85]
print(35 in marks)


print(25 not in marks)
'''
'''print('code' in 'gnan')
print('$' in 'abc$frg')

#Logical operators -->logical decision making --> and,or,not
#and -->all conditions to be satified
#or --> any one condiotion to be satisfied
a = (25 in [25,45,65]) and 45 < 56
print(a)

b = 45 > 56 or 25 <= 45
print(b)

c = not(True)
print(c)

'''
'''#Identity operators --> check for identity of an object --> id()
#is  ,is not
a = 35
b = 35
print(id(a))
print(id(b))
c = a
print(id(c))
print(c is a)


a = [1,3,4,5]
print(id(a))
c = a
print(id(c))
print(c is a)

b = [1,2,3,4,5]
print(b)
'''









