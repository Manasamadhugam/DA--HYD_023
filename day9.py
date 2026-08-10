'''
Strins --> caseConversions.Searching & finding,String testing methods,
Replace,Space removal

#Searching,Finding,Replacing,Joining...
a = "Codegnan"
print(len(a))
print(min(a))
print(max(a))

b = a.index('g') # it returns the index position
print(b)
c = a.index('n') #it returns only the first occurance
print(c)
d = a.index('n',6) #it returns the next occurance
print(d)

#e = a.index('n',8) #ValueError
#print(e)
#f = a.index('t') #ValueError
#print(f)
g = a.index('n',2,6)
print(g)
g = a.index('n',1,4)
print(g)


#rindex() --> returns last occurance
b = a. rindex('g')
print(b)
c = a.rindex('n') #here 'n' is occuring at 7th index
print(c)
#d = a.rindex('n',8) #it returns ValueError
#print(d)


#count() --> returns the number of items object is repeating
print('Codegnan'.count('n'))
print('code'.count('w')) #it returns 0 as we dont have 'w' in 'Code'
print('Cakshjasaksajs'.count('a'))

#find()  -->first occurance but it avoid error returns -1 if substring is
#not found
print('Codegnan'.find('r')) #it returns -1
print('codegnan'.find('n'))
print('codegnan'.find('e'))
print('codegnan'.rfind('g'))


a = "DataAnalysis"
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.rindex(i))

#Replacing,Splitting,Joining
#Strings are Immutable means it cannot be modified
a = 'Codegnan'
#a[4] ='s'
a =  a.replace('g','s')
print(a)
a = a.replace('g','s')
print(a)
print('fggfdhyfgdesghug#eyhugy#tfytf'.replace('#',''))
print(a.replace('x','manasa'))

a = 'code manasa python'
print(len(b))
b = a.split() #by default if we have space if splits (returns list)
print(b)
print(len(b))

c = 'code,manasa,python'
d = c.split()
print(d)

e = c.split(',')
print(e)

#join()
a = 'code'
b = 'gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('manasa'))
print(' '.join('mokshith'))

#String testing methods (boolean) can be true or false
#isalpha(),isalnum(),isdigit(),isupper(),islower().....

a = 'Codegnan123'
print(a.isalnum()) #returns True for alphanumeric strings else false
b = 'Codegnan'
print(b.isalnum())
print(a.isalpha()) #returns True only for alphabets
print(a.isdigit()) #returns True only for digit string
print('9876543210'.isdigit())
print('2345'.isnumeric()) #this has upper edge (numbers,fractions,romans)
 #startswith() --> how its starting
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))

print('codegnan'.islower()) #returns true for all lowercase
print('Codegnan'.isupper()) #returns True for all uppercase
print('Codegnan Python'.istitle())

#Space removal --> strip() (removes leading and trailing spaces)

a = 'codegnan'
print(a.strip())
b = input("Enter the string:").strip().lower()
print(b)
'''
#zfill() filling with zeros as per the given numeric string
print('234'.zfill(4))
print('234'.zfill(8))

print('hai'.center(6))
print('hai'.center(6, '#'))

print('hai'.ljust(6, '#'))
print('hai'.rjust(6, '#'))




















































