'''
Identity Operators --> checks the identity of an object --> id()
'''
'''
a = 5
b = a
print(id(a))
print(id(b))
c = 5
print(id(c))
print( a is c)
print(5 == 5)
'''
'''
a = [1,3,5,6]
b = a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))

#As we have Lists (mutable Collection) both c and a lists will have different
#ids whereas values are same
print(c is a) #output False
print(c == a) #output  True
print( a is not c)
 '''
'''#Bitwise operators --. we perform bitwise operations over operands
#& (and) , (or),^(XOR),shifting operators (<<,>>)
#Number will be converted to inary and bitwise and is perform
print(5 |3) #bitwise OR
print(5 ^ 3) #Bitwise XOR

print(5 and 3) #here and is logical operator checks for both existances
#returns 5 in above case

print(5 or 3)

print(5 and 0)

print(5 or 0)
'''
'''
#Leftshift operator << ,Right shift operator

print(5 < 1) #false comparison
print(5 << 1) #left shift operation by 1 position
print(5 >> 1)#Right shift operation
print(15 << 2)#convert is to binary and perform 2 times left shifting
print(15 >> 2)#same 2 times right shifting
'''
'''
#Input formatting --> input(),int(input()), float(input())
#you know  -->single input
#2 or 3 inputs --> map()
#group of integres --> list(map(int,input().split(','))
names = input("enter the names:").split(',')
print(names)

name1,name2 = map(str,input("enter the friends names:").split(','))
print(name1,name2)
'''
#Tokens --. Numeric datatypes --> operators --> flow of the program
#Control Block Statements --> they control the flow of the program
#when to execute,hw to execute
#Condition Statements --. if,else,elif (rely on conditon to be executed)
#repetition ststements (Loops) --> for,while

#Conditional Statement --. if usage
'''
Syntax :
if <condition>:
statements(s)...
......
'''
'''#age = 15
age = int(input("enter the age:"))
if age >18:
    print('your age is:',age)

age = int(input("enter the age:"))
if age>=18 and age in [19,21,20]:
    print('your age is',age)
print(age)
'''
'''
else:
    statement(s)..
 f ,condition>:
    statement(s)...
    ....
 else:
     statement(s)..
     ..
'''
'''#Vote elibility -. To check his/her voter eligility and give access...
age = int(input("enter the age"))
if age>=18:
    print("you have Voter eligibility and age is", age,"years")
    print("access Granted")
else:
    age = 18-age
    print("you dont have eligibilty as your age is",age,"years")
print("you need to more",age,"yeras")

#Same case let's use only nested -->if,else
if age >0:
    if age>=1
        print("you have Voter eligibility and age is", age,"years")
        print("access Granted")
else:
            age = 18-age
print("you dont have eligility as your age is",age,"years")
print("you need to wait for",age,"more years")

else:
print("you have entered -ve values/zero enter only =ve")
'''
    


#Task : Student marks and grade analyzer
#90 - 100 ---> "A"
#80 - 89 --> "B"
#70 - 79 --> "C"
#60 - 69 --> "D"
#<60 --> Fail
#also -ve cases sholud not be allowed and marks shouldn't be in -ve values
marks = int(input("enter student marks:"))
marks = int(input("Enter student marks: "))

if marks >= 0 and marks <= 100:
    if marks >= 90:
        print("Grade: A")
    else:
        if marks >= 80:
            print("Grade: B")
        else:
            if marks >= 70:
                print("Grade: C")
            else:
                if marks >= 60:
                    print("Grade: D")
                else:
                    print("Fail")
else:
    print("Invalid Marks")

    
            
        


 
    
            










 






















