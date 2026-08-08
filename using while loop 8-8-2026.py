'''
# write a program for the guess number
secret = 2900
guess = int(input())
while guess != secret:
    if guess < secret:
        print("To Low")
    else:
        print("Too High")
    guess = int(input())
print("Correct guess")


#Otp verification
otp = "2222"
max_attempts = 7
current_attempts = 0
while current_attempts < max_attempts:
    entered_otp = input("Enter the otp:")
    if entered_otp == otp:
        print("log in successful")
       
    else:
        print("Entered otp not valid")
        current_attempts += 1
else:
    print("Entered otp is fail")


#food order system
food = input("enter the item:")
count = 0
while food != "Exit":
    count += 1
    food = input()
print("Total no.of items ordered",count)
'''

#to win the game 3 chances
chances = 3
while chances > 0:
    answer = input("Enter the correct answer:")
    if answer  == "python":
        print("You won the game!")
    else:
        chances = chances - 1
        print("You have", chances, "more chances")
else:
    print("You lost the game!")
        
    

    










































