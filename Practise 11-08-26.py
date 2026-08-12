'''
#Text Case Converter

text = input("Enter a sentence:")
methods = [text.upper(),text.lower(),text.title(),text.capitalize(),text.swapcase()]
for x in methods :
    print(x)
if text.isupper():
    print("Uppercase")
elif text.isloweer():
    print("Lowercase")
elif text.istitle():
    print("Titlecase")
else:
    print("Mixed case")
   
        
#Username Validator
while True:
    username = input("Enter username:")
    if username == "quiet":
        break
    print("Alphanumeric:",username.isalnum())
    print("Begins with letter:",username[0].isalpha())
    print("Valid identifier:",username.isidentifier())
    print("ASCIL:",username.isascil())


#Formatted Student Report
print("STUDENT REPORT")

for i in range(3):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"

    print(name.ljust(10), str(marks).rjust(5), grade.rjust(5))
'''

# Character and Text Analyser
text = input("Enter a line of text: ")

letters = 0
digits = 0
spaces = 0
printable = 0
non_printable = 0

for ch in text:
    if ch.isalpha():
        letters += 1

    if ch.isdigit():
        digits += 1

    if ch.isspace():
        spaces += 1

    if ch.isprintable():
        printable += 1
    else:
        non_printable += 1

print("Letters       :", letters)
print("Digits        :", digits)
print("Spaces        :", spaces)
print("Printable     :", printable)
print("Non-printable :", non_printable)

print("Lower case    :", text.islower())
print("Upper case    :", text.isupper())
print("Title case    :", text.istitle())
    
#Done


    




































