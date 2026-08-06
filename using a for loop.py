'''# using for loop

products = list(map(int,input("Enter the price:").split(',')))
total = 0
for i in products:
    total = total + i
print(f'sum of 4 items is --> {total}')
              
password = input("Enter the password:") 
upper = lower = digit = special = 0
for ch in password:
    if 'A' <=ch<= 'Z':
        upper += 1
    elif 'a' <=ch<= 'z':
        lower += 1
    elif '0' <=ch<= '9':
        digit +=1
    else:
        special += 1
print("Upper:", upper)
print("Lower:", lower)
print("Digit:", digit)
print("Special:", special) 
'''
#extraction og 'gmail.com' from email id
email = input("enter e-mail:".split(','))
for mail in email:
    print(email.split("@")[1])


























