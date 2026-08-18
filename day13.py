'''
Mapping --> Dictionary --> Collection of key -value pairs used to store
related data --> JSON,APIs,database records

dict() --> data = {}
Dictionary is Mutable, Indexed through keys, Ordered, Heterogenous,
Keys must be Unique (int,strings,float values...)
'''
 
'''
details = {}
print(type(details))

details = {'Id' : 'CHG4022','name': 'Manasa',
           'Gender' : 'F', 'Age':20,
           'Batch': 'DA23','Place':'Hyd'}
print(details)
print(len(details))
'''
'''
#Access the data from dictionary
#details[0]  #KeyError

print(details.keys()) #it returns keys from the dictionary
print(details['Id'],details['name'])
#if key name is not matching /invalid
#print(details['marks']) #KeyError as marks is not present
details['marks'] = []
print(details)
print(type(details['marks']))
details['marks'].append(20)
print(details)

details['marks'].extend([15,20,25,20,20])
print(details)

#create a key-value pair of Practise Session
details['PS'] = ('Tueday','Thursday','Saturday')
print(details.keys())
print(details['marks'][2])
#Accessing 2nd day of Practice session
print(details['PS'][1])
details['MI'] = ('Monday','wednesday','Friday')

#operations -->mutable,indexing through keys,membership

print('Wednesday' in details)
print('MI' in details) #returns True as we have MI as key
for i in details:
    print(i) #returns keys one by one


for i in details.keys():
    print(f'Key = {i}')
    print(f'Value = {details[i]}')

#keys() --> returns keys from the dictionary


for i in details.values(): #returns value from dictionary
    print(i)

for i in details.items(): #returns a key-value pair
    print(i)
for key,value in details.items():
    print(f'key is {key}')
    print(f'Value is {value}')

#update()
details.update({'marks':[], 'PS': ('Tuesday','Thursday','Saturday')})
print(details)
details['marks'].extend([25,30,25])
print(details)
marks = list(map(int,input("Enter the marks:").split(',')))
print(marks)
details['marks'].extend(marks)
print(details)


print(details.keys())
print(details.get('name'))
print(details.get('Branch')) #it returns None as we dont have Branch as key
print(details.keys())

details.setdefault('Branch') # if key is not present it inserts into dict
print(details)
details['Branch'] = 'AIDS'
print(details)

print(details.setdefault('name'))
print(details.keys())

print(details.pop('Branch'))  #we need to mention key
print(details.keys())

print(details.popitem()) #removes and return a key, value pair as a 2- tuple
print(details.popitem())

del details['Id']
print(details.keys())

details.clear() #removes all elements from 0
print(details)


#fromkeys() --> creates a dictionary from iterable (lists,tupes,sets,string)
data = ['manasa','pandu','ashu']
b = dict.fromkeys(data) #creates a dict but value set to None
print(b)
b['manasa'] = 31
print(b)
c = dict.fromkeys(['CGH1234','CGH2345'],['code','gnan'])
print(c)
'''

#task: Create a dictionary with your personal details,similar to your
#Codegnan profile

profile={'Name':'Manasa',
         'ID':'CGH4022','batch':'DA-HYD-023',
         'DOB':'2004-08-29',
         'age':21,'gender':'female',
         'state':'telangana','no.':7013154229}
print("personel details",len(profile))
for key,value in profile.items():
    print(key,':',value)

profile.update({'college_Name':[],
                'degree_pass% ':[],
                'SSC_pass%':[],
                'INTER_pass%':[]})
profile['college_Name'].append(input("enter degree college name:"))
profile['degree_pass% '].append(int(input("enter marks")))
profile['SSC_pass%'].append(int(input("enter marks")))
profile['INTER_pass%'].append(int(input("enter marks")))
for key,value in profile.items():
    print(key,':',value)
    














































