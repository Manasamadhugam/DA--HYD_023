'''
#Students Marks manager -1
marks = []
for i in range(3):
    mark = int(input("Enter the mark:"))
    marks.append(mark)
print("Original marks:",marks)
marks.insert(0,90)
marks.extend([75, 85])
if 75 in marks:
    marks.remove(75)
removed_mark = marks.pop()
print("Removed mark:", removed_mark)
print("Final marks:", marks)
print("Number of marks:", len(marks))
'''    
'''
#Number List Analyser -2
numbers = [20,10,30,20,40,20]
numbers.sort()
print("Ascending order:", numbers)
numbers.reverse()
print("Descending order:", numbers)
num = int(input("Enter the number:"))
if num in numbers:
    print("Number is available")
    print("Count:", numbers.count(num))
    print("Index:", numbers.index(num))
else:
    print("Number is not available")
'''  
'''
#Even and Odd Number Separator-3
numbers = [10, 15, 20, 25, 30,35]
even = []
odd = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:",even)
print("odd numbers:", odd)
print("First 2:", numbers[:2])
print("last 1:", numbers[-1:])
backup = numbers.copy()
numbers.clear()
print("Original list:", numbers)
print("Backup list:",backup)
'''
'''
#Unique Name Manager-4
names = ["Ashu", "Srivan", "Ashu", "Nandhu", "Srivan"]
names = set(names)
print("Unique names:", names)
names.add("mansa")
names.update(["Aruna","pinky"])
if "Nandhu" in names:
    names.remove("Nandhu")
names.discard("Pandu")
for name in names:
    print(name)
'''

'''
# Course Student Comparison -5
python_students = {'Asha','Rahul','John','Meera'}
da_students = {'Rahul','Meera','Arun'}
print('both courses:',python_students | da_students)
print('both courses students:',python_students & da_students)
print('only python:', python_students - da_students)
print('only one course:', python_students ^ da_students)
print('DA subset of python:',da_students.issubset(python_students))
print('python superset of DA:', python_students.issuperset(da_students))
print('Disjoint:', python_students.isdisjoint(da_students))
print('common students:')
for student in python_students & da_students:
 python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}
print("Union:", python_students.union(da_students))
print("Intersection:", python_students.intersection(da_students))
print("Only Python:", python_students.difference(da_students))
print("Only one course:", python_students.symmetric_difference(da_students))
if da_students.issubset(python_students):
    print("DA is a subset of Python")
else:
    print("DA is not a subset of Python")
if python_students.issuperset(da_students):
    print("Python is a superset of DA")
else:
    print("Python is not a superset of DA")
if python_students.isdisjoint(da_students):
    print("Students are disjoint")
else:
    print("Students are not disjoint")
print("Students learning both:")
for student in python_students.intersection(da_students):
    print(student)
'''




























