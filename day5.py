
'''
marks = int(input("Enter the marks (1 -100):"))
if marks > 0 and marks <=100:
    if marks >= 90: 
        print("User has secured Grade A")
        if marks >= 80  and marks <= 89:
            print("User has secured Grade B")
            if marks >= 70 and marks <= 79:
                print("User has secured Grade C")
                if marks >= 60 and marks <= 69:
                    print("User has secured Grade D")
                if marks >= 60:
                    print("User has failed,study again")
else:
    print("Enter only +ve values greater than 0 and less than 100")
    '''

#elif keyword --> if-elif-else
'''
    if<comdition1>:
            statements(s)...
            .......
            elif<condition2>:
                statements(s).....
                elif,condition3>:
                statements(s)...
                else<condition3>:
                statements(s).....
                '''

                
'''
marks = int(input("Enter the student marks:"))
if marks < 0 and marks > 100:
            print("Entered values should be greater than 1 and less than 100")
elif marks >= 90 and marks <=100:
    print("use has secured Grade A")
elif marks >= 80 and marks <=89:
 print("use has secured Grade B")
elif marks >= 70 and marks <= 79:
 print("Use has secured Grade C")
elif marks >=60 and marks <= 69:
 print("Use has secured Grade D")
elif marks<=60 and marks >=0:
 print("Use has failed, study again")
else:
 print("No negative values")
                                                 '''


'''
age = int (input("Enter the age:"))
if age>=18 and age <=100:
    print('----- User has vote Eligibility -----')
    print('----- Access Granted -----')
elif age<18 and age >0:
    print('----- User still need to grt Vote Eligibility  -----')
    print('-----User need to wait for more',(18-age), 'year(s)-----')
else:
    print('-----Only +ve values and less than 100 acceptable-----')

#prefer if-elif-else....
'''
    

'''
#Output Formatting -->old  style formatting (using commas)
#Output formatting --> old style formatting (using commas)
#% usage (%f,5d),, format() usage,fstring notation
a,b = 7,9
print(a)
print(b)
print(a,b)
name = "codegnan";batch = "DataAnalysis"
print(name,batch) #by default sep is having space
print(name,batch,sep= ',')
print(name,batch,sep='------>')
#end = '\n' ,\t --> tab space
print(name,batch,end='\t')
print(a,b, end= '  ')
print("hyderabad")
'''

'''name='Codegnan';age=7;batch='DA-023';place='Hyderabad'

#usage of commas
print(batch, 'is in',name) #variables and msg to be separated by comma
print(name, 'is in ', place, 'age is',age, 'years')
                                                 
#Old style formatting --. %d --> integer, %s --> string, %f --> float
salary = 25000
print("His Salary is %d"%(salary))
print("His Salary is %f"%(salary))
                
salary = 24253.256
print("His Salary is %d"%(salary))
print("His Salary is %f"%(salary))
                          
print("His Salary is %.1f"%(salary)) #%.if --> rounding to 1 decimal

#.format() usage
print("{} is in {}".format(name,place)) #order matters

#fstring usage (more recommended)
print(f'{name} is in {place}')
print(f'{"manasa"} is in {name}')
'''
'''
color = input("Enter the color")
if color == "red": 
    print('stop')
elif color == "yellow":
    print('ready')
elif color == "green":
        print('go')
'''

fruits = input("enter the fruits")
if fruits == "apple":
    print('red')
elif fruits == "banana":
    print('yellow')
elif fruits == "grape":
    print('black')
                          
            
            

                
                     












































 
