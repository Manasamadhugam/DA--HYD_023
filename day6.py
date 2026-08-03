'''
Control Statements --> contril of Flow of excution of the program
          --> Conditional Statements --> if,elif,else...
    --> repetition Statements(Loops) --> for,while(for with else) (while with else)

    --> Jumping Statements -->break,continue,pass
'''
#Loops --> loops are helpful for repetition (Automative tasks)
#for keyword will be helpful to iterate over a sequence / range
#Syntax for (for keywoed):
'''
for 
<temp_var> in sequence/range:
    statement(s)....
    .....
'''
'''
#range(stop) -->default 0 ends at stop-1
#range(start,stop,step)
#by default range picks 0 as start value
for i in range(10):
    print(i)
    '''
'''
#In above case we got 10 iterations
for i in range(1,10):
    #if i > 5:
        #print(f'value of i is -->{i}')
    #Now i want to get only even numbers with above condition
    if i > 5 and i%2 == 0:
        print(f'final value of i is --> {i}')
        '''
'''
#range(start,stop,step) -->here step --> interval..
for i in range(1,10,-1):
    print(i)
    print("Done")
    '''
'''
for i in range(10,0,-1):
    print(i)
 '''
'''
#Print -10 to -1
for i in range(-10,-1):
    print(i)
for i in range(-10,-0):
    print(i)
    '''
'''
#[] --> we generally Lists
names = ['sathyam','mokshith','laxmi']
print (len(names)) #len(obj) --> returns the number of items in a container
for name in names:
#print(name)
#print(f'Student name is {name}')
     name == "mokshith":
         print(f"Student name is {name}')
               '''
#Calculate the sum of first 10 numbers
#first understand your input --> range(11) --> 10 numbers
#second understand your output --. sum (number)
#third we need to map the logic

result = 0 #target variable
for i in range(11):
    #print(i)
    #print(f'result is {i+i}')
    result = result + i #result += i
    print(f'Now the result is {result}')
print(f'Sum of 10 numbers is {result}')

print(f'sum of 10 even numbers is {result}')


'''
#Sum of first 10 even numbers   
result = 0 #target variable
for i in range(21):
    if i %2 == 0:
        result = result + i #result += i
        print(f'sum of 20 even numbers is {result}')
        '''
#Understand the usage with Fitness streak example
#work_out -->, work_out_missed --> 0

work_log = [0,1,1,1,0,1,0]
#result variable --> longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 3:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
    else:
        current_streak = 0 #streaks breaks
        print(f'longest Streak is {longest_streak}')
        



























































































                                  
