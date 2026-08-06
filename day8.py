'''
Tokens -->keywords,identifiers,literals,Operators,Punctuators,Variables
operators -->Numeric data (int,float,complex) ,bool
Control flow -->if,elif,else,for,while
Sequences -->strings,lists,sets,tuples,mapping(dict)

#Strings --> Group of characters we use single or double or triple quotes
#for representation of strings...
# strings are Immutable,Ordered,Indexed Collection
'''
'''
name = 'Codegnan'
print(name)
print(type(name))
print(len(name)) #len -->returns the number of items in container

#index() -->fetch the object (position) starts at 0 and ends at len(obj)
#we use [] representation
print(name[0])
print(name[5])
#print(name[25]) #Indexerror --> as its out of range


#Negative Indexing --> -1 to len(obj)
print(name[-1]) #it returns last character
print(name[-3]) 
print(name[-33]) # indexerror


#Slicing --> we can access group of characters(objects)
#we use [start:end] #start default --> 0,start is included,end is excluded

print(name[:]) #returns entire string
print(name[0:]) #returns entire string
print(name[1:4]) #starts at 0th index before 4th index
print(name[1:5])

name = 'manasa'
print(name[1:4])
print(name[0:4])
print(name[0:7])


name = 'python'
print(name[3:7])
print(name[7:3]) #returns empty as strings are immutable
#Slicing is applicable from lower index to higher index
print(name[:45]) #returns till end of the string 
print(name[45:])

print(name[-1:-5]) #returns empty string
print(name[-5:-1]) #starts at -5 and ends at -2

#print 'on' from above string
print(name[4:1])
print(name[4:6])
print(name[-2:])

name = 'mokshith'
print(name[0:9])
print(name[1:6])
print(name[1:-2])
print(name[-9:-0])
print(name[2:-6])
#observe +v +ve, -ve-ve, & +ve,-ve all posibilities

#Striding --> [start;end:stop]
course = 'DataAnalysis'
print(len(course))
#Data -->result
print(course[:4])
print(course[4:])
print(course[-3:1])

print(course[::1]) #returns all characters
print(course[::2]) #includes start to end skipping character

print(course[1:6:3])
print(course[1:6])
print(course[2::3])

print(course [::-1]) #it returns the reverse of a string
print(course[::-2])

name = 'Codegnan'
#name[3] = 'w' #Strings are immutable
#Operations on Strings --> Indexing,Concatenation,Repetition
print(name * 3)
print('*' * 25) #repetition

#Concatenation --> combining strings
data = 'aruna' + 'python' + 'database'
print(data)

print('123' * 4) #Numeric string
print('code' in 'codegnan')
for i in 'Codegnan':
    print(i, ':')

for i in 'codegnan':
    print(i,end= ' ')

name = "datacodegnan" 
#Built -in functions --> len(),min(), max(),sorted()
print(len(name))
print(min(name))
print(ord('A'))
print(ord('a'))
print(chr(97))
print(max(name))
print(sorted(name)) #returns a list by sorting all elements
'''

#Methods on strings --> case- Conversions,Finding/Searching...
name = 'codEgnan data'
#Case-conversions --> upper(),lower(),title(),capitalize()
a = name.upper()
print(a)
a = name.lower()
print(a)
a = name.title()
print(a)
#Capitalize() it converts first letter to uppercase
c = name.capitalize()
print()
d = name.title()
d = name.title() #converts every werd first letter to uppercase
print(d)
















