'''
Lists, Tuples..
#List --> mutable,Ordered,Heterogenous
#index(),count(),copy(),sort(),reverse()
details =['codegnan',7,2018,'hyderabad']
print(len(details))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21)) #it returns first occurance
print(details.index(21,6))
#print(details.index("python')) #ValueError
print(details.count(21))
print(details.count('python')) # it returns 0 as we dont have it

#copy() -->shallow copy of the given collection
new = details.copy()
print(new)
print(type(new))
print(details)

new[2] = 'Agentic AI'
print(new)
print(details)
details.append(124)
print(details)
print(new)


data = [1,4,5,[21,34,45],23]
print(data)
new = data.copy()
print(new)
new[3][2] = 'Agents'  #whenever we  make changes in nested list original will
#also be effected
print(new)
print(data)

new[1] = 'python'
print(new)
print(data)
'''
'''
marks =[14,24,-45,27,35]
print(marks)
print(marks.sort()) #returns None
print(marks) #returns in ascending order
marks.sort(reverse = True) #returns in Descending order...
print(marks)

marks.insert(4,'mansa')
#marks.sort()
#reverse() --> returns in reverse order
marks.reverse()
print(marks)



print(marks[::-1])
'''
'''
#type(),len(),max(),min(),print()
print(sorted('manasa')) #returns List in ascending order
#print(sorted(['code','23',45])) #raises Error
'''
'''
#Tuples --> Tuples are Indexed,ordered,Heterogenous,Immutable collection
#dimensions,coordinates,database records, we prefer () for tuple notat

a = ()
print(type(a))
print(len(a))

dimensions = 1.5,2.5
print(dimensions)
print(type(dimensions))
print(len(dimensions))
'''
'''
#Operations --> Indexing,Slicing,Striding,membership,merging,Repetition
courses = ("PFS', 'JFS",('DA','DS'),'Agentical AI',[100,6,6])
print(courses)
print(len(courses))
print(courses[-1][2])
print(courses[-2][-2:])

#coueses[2] = 23 Tuples are Immutable
courses[-1].append('codegnan') #we can make any modifications inside list
print(courses)

#Create a Nested tuple as above and work on Slicing,Striding and List Function
print('PFS' in courses)
d = courses * 2
print(d)
e = courses + (2,3,4,5) #merging 
print(e)
'''
'''
#Tuples Immutable --> count(), index()
print(courses.index('Agentical')) #returns first occurance
print(courses.count('Agent'))

#print(courses.sort()) #attributeError  --> sort() is in Lists not in Tuples

print(sorted(courses[-1]))
#print(sorted(courses)) #as we have mixed type

d = sorted((23,12,3,4,5))
print(d)
'''
'''
#accept group of integers space separated
a,b = map(int,input("Enter the values").split())
print(a,b)

a = tuple(map(int,input("Enter the values").split(',')))
print(a)'

print(eval('9 + 4'))
a = eval(input("Enter a list"))
print(a)
print(type(a))

#Task: Take a user input as string, do this in two ways.

1) give the count of each repeating character
test case 1: programming
r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2)
r is repeating 2 times
index = [1,4]
g is repeating 2 times
index = [3,10]
m is repeating 2 times
index = [6,7]
'''
#1st test case

s = input("Enter a string: ")

for ch in set(s):
    count = s.count(ch)
    if count > 1:
        print(f"{ch} is repeating {count} times")

print()

#2nd test case
for ch in set(s):
    indices = [i for i, c in enumerate(s) if c == ch]
    if len(indices) > 1:
        print(f"{ch} is repeating {len(indices)} times")
        print(f"index = {indices}")































