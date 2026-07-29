'''
Tokens --> variables, Punctuators
variables --> Named memory location, its a placholder for data
#Rules are to be follwed
'''
#MultiAssignment of variables
name,age,place = 'Codegnan',7,'Hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='------>')

#a,b = 2,4,5
#Reassigning variables
name = "Codegnan"
a,b = 45, 1.5
print (a,b)
a,b = b,a
print (a,b,sep=',')
b,c = 10,20
print(b,c)
a,b = b,c
print(a,b)
#deleting the variables -->del
#del a
#print(a)
#print(a,b)
'''
#punctuators --> [](Lists),()(tuples),{}(Dict, sets)
name = "Codegnan"; age = 7;course = 'Data analytics'
print(name,age,course)

#Datatypes --> Numeric (int,float,complex),boolean, none
# --> Sequences --> Lists,Tuples, Sets, Strings,
#Frozensets, mapping(dict)
#Numeric type --> int,float,complex
#int datatype --> quality,age..
age = 7
print(age)
print(type(age)) #type --> returns the datatype of object
print(type(234))
#quality =03 #it not allowed
#print (quality)

#discount = 2.5
print(price,discount)
print(type(price))
'''
'''
#complex -->combination of real and imag
i2 = 4
data = 5 + i2
print(data)

data = 5+2j #j is imag representation
print (data)
print (type(data))

  #Boolean --. true / False
valid  = True
print(type(valid))
error = False
print(type(error))


#Typecasting --> Converting one type to another type
#Python by default follows Implict Type (we need not mention the datatype)
#we will go for explict conversion
# Every built- in datatype is a built-in function
int, float, complex, bool
#Typecasting --. int --> float,complex,bool
age == 35
print(type(age))
b = float (age)
print(b)

c = complex (age)
print(c)
d = bool (age) #returns True for existing data
print(d)
e = bool(0)
print (e)
'''
#Float --> Typecasting
age = 35.55
print(type(age))
b = int(age)
print(b)
c = complex (age)
print(c)
d = bool (age) #returns True for existing data
print(d)
e = bool(0)
print (e)
'''
#complex --> Typecasting --> int, float,bool
data = 2+5j
print(type(data))
#b = int(data) #TypeError
#print(data)
#c = float(data)
#print(c)
d = bool (data)
print(d)
print(type(d))
'''
e =int (float(bool(45)))
print(e)
a = bool(float(int(25)))
print(a)

f = 45+ 2.5 + 2 + 3j + False
print(f)































































