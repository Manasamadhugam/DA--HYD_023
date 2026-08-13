'''
Sequences --> Strings,Lists,Tuples,Sets
Mapping --> Dictionary

#Lists -->Collection of heterogenous elements (items)
#List -->Indexed,Ordered,Mutable,Heterogenous,we use [] to store the data

marks = [35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in mark)
#Operations : Indexing,Slicing,Striding,Membership,Merging,Repetition
'''
'''
#Nested Lists -->  A list inside another list
names = ['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(len(names))
print(names[0])
print(names[3])
print(names[-3])

print(type(names[0]))
print(names[0][:4]) #it returns Code
print(names[0][4:])

#get the output as Cdga
print(names[0][::2])
names[0] = names[0][::-1]
print(names) '''
'''
print(names[3])
print(len(names[3]))
print(names[3][2])
#Indexinh,Slicing --> Mutable
names[2] = 'Python'
print(names)
#By indexing if we change the elements,length of collection will remain same
names[4] = ['Codegnan','PFS','JFS','DA','AAA','DS']
print(names)
print(len(names))
print(names[3][1:3])

names[2:4] = 'Manasa','Mokshith','Ashwini','Sathyam'
print(names)

#In Slicing elements u pass as per the logic length keeps on increase
names[3:6:2] = 'pyhton','java'
print(names)


#Create a nested list with strings ,lists and work on Indexing ,Slicing,Striding
#Added advantage if u could add string functions also to it
#Lists Functions -->append(),extend(),pop(),remove(),clear()
#index(),count(),copy(),sort(),reverse()


names = ['Codegnan','mansa']

#append() -->inserts single to the end of the list

names.append('data')
#print(names)
#names.append('analysis','agents') #TypeError

names.append(['analysis','agents'])
#print(names)
#append will always increment the length of list by 1
#print(names[3])
#(names[3].append('chatgpt')) #it returns None as append is applicable
#on list not print 
print(names)

#extend() -->inserts multiple elements in the end of list
names.extend('analysis') #string will be splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,75,24,56])
print(names)
#names.extend(35,45) TypeError
#print(names)


#insert(index,object)-->inserts given object before index
names.insert(1,'python')
print(names)
names.insert(0,'java')
print(names)

#names.insert([1:4],['a','b']) #SyntaxError
print(names)
names.insert (-1,'AAA')
print(names)

#pop(),remove(),clear()
#pop(0 by default last,else given index
print(names.pop())
print(names)
names.pop(2)
print(names)

#remove(0 we can remove a specific value
names.extend([23,14,15])
print(names)
names.remove(14)
print(names)
names.remove(14) #it raises valueError

del names[1:3] #del keyword will apply permanent changes
print(names)
names.clear() #clear() will remove all elements and returns empty list
print(names)
'''

data = ['codegnan', 'manasa', 'pandu', 'ashwini']

for i in range(len(data)):
    print("Index", i, ":", data[i])
































































        
         



















































