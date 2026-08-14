'''
Sequences --> Sreings,Lists,Tuples,set,Frozenset
Mapping -> Dictionary
'''
#Sets --> A Set is a unique Collection of objects,Unordered,Mutable,
#Hashing,Unindexed,Unique,Heterogenous 
#set() ,{}
#a = {} its an empty dictionary
'''
a = {}
a = set()
print(type(a))
stud_ids = {123,345,234,564,234}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))

#print(stud_ids[2]) #TypeError
print(234 in stud_ids)
#print(stud_ids *2)
print(stud_ids + stud_ids) #Two sets cannot be merged
'''
'''
data = {3,4,5,(12,3,4),'manasa'}
print(data) #No lists inside a Set (hashing technique) Lists are Mutable
data = {3,4,5,(123,4),'manasa'}
print(data)
print(len(data))
for i in data:
    print(i)
'''
'''
#Methods on sets -->add(),update(),remove(),discard(),pop()
'''
names = {'manasa','pandu','mokshith','ashwini'}
'''print(len(names))
#add() will insert an element into the set (it can be anywhere but only unique)
names.add('python')
#names.add('manasa','bobby')
#print(names)
names.add(('poll','police'))
print(names)
'''
da_names = {'sathyam','laxmi','pandu','vikram'}
'''
#update(0 we can update multiple elements (set)
names.update(da_names)
print(names)
print(da_names)
da_names.update(names)
print(len(names))
print(len(da_names))
'''
'''
#remove(),discard(),pop(),clear()
da_names.remove('pandu')
print(da_names)
#da_names.remove('pandu') #KeyError
#discard() will remove an element if its present else it ignores
da_names.discard('anil')
'''
'''
da_names.pop()
print(da_names)
print(da_names.pop()) #removes and returns an arbritary element
print(da_names)
da_names.clear()
print(da_names)
da_names.add('Madugam')
print(da_names)
da_names.updat#e(['pandu','manasa'])
print(da_names)
'''
'''
#copy()
d = da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)
'''
'''#mathematical operations -->union(),intersection(0,differance(),symmetric_d
#issubset(),issuperset(),isdisjoint()
da_23 = {12,23,34,45,23,36}
da_24 = {34,46,47,23}
event = da_23.union(da_24)
print(event)
print(len(event))
common = da_23.intersection(da_24)
print(common)
print(len(common))

common = da_23.intersection_update(da_24)
print(common) #it returns None
print(da_23) #common elements are finally stored

print(da_23)
print(da_24)
#differnce() removes common elements and prints rmng elements from first set
#diff = da_23.difference(da_24)
#print(diff)
#f = da_23 - da_24
#print(f)
#symmetric_diffrence() -->removes common elements and prints all rmng
#elements from two sets
sym = da_23.symmetric_difference(da_24)
#print(sym)
h = da_23 ^ da_24
#print(h)

#issubset() -->checks for all elements to be present in other set
da_24.remove(46)
da_24.remove(47)

print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))

#isdisjoint() returns False for sets having common elements
print(da_23.isdisjoint(da_24))
'''
#length of Unique student in aclass,where user can enter first input
#he should be giving number of student_ids,he will enter student_ids
n = int(input())
student_ids = input().split()
#print(student_ids)
result = set (student_ids)
print(len(result))



























