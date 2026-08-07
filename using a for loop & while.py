'''score =int(input("Enter the number of balls: "))
total_score = 0
for i in range(score):
    run = int(input("Enter runs:"))
    if run == 0:
        print("Dot Ball")
    elif run == 6:
        print("Boundary")
    else:
        total_score = total_score + run
        print("Total Score:", total_score)


runs = list(map(int,input("Enter the number:").split(',')))
total_score = boundaries = dotballs = 0
for i in runs:
            total_score += i
            if i == 4 or i == 6:
                boundaries += 1
            elif i == 0:
                dotballs +=1

print("boundaries:", boundaries)
print("dotballs:" , dotballs)
print("total_score", total_score)


#wtite the program of a pattern unlocking using while looop

pin = "2908"
max_attempts = 5
current_attempts = 0
while current_attempts < max_attempts:
    entered_pin = input("Enter the pattern:")
    if entered_pin == pin:
        print("phone unlocked!")
       
    else:
        print("Entered pin is fail_attempts")
        current_attempts += 1
else:
    print("Entered pin is fail... Try again after 1 minutes...")
    '''


pin = "2110"
max_attempts = 3
current_attempts = 0
while current_attempts < max_attempts:
    entered_pin = input("Enter the pin:")
    if entered_pin == pin:
        print("log in successful")
       
    else:
        print("Entered pin not valid")
        current_attempts += 1
else:
    print("Entered pin is fail")


        
    


    
