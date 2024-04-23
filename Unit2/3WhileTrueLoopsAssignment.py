# ========== 2.3.1 ==========
# print("Hi")

# while True:
#     print("Hi")
#     yes=input("Shall we continue: ")
    
#     if yes== ("no"):
#         break

# print("okay then")
 


# ========== 2.3.2 ==========
# from math import sqrt 
# while True:
#     number=int(input("Please type in a number: "))
#     if number == 0:
#         break
#     elif number < 0:
#         print("Invalid number (must be positive)")
#     else:
#         print ("The square root of", number, "is", sqrt(number))
    
# print("Exiting...")
# ========== 2.3.3 ============

# number=int(input("Countdown!"))
# while True:
#   print(number)
#   if number==0 :
#     break
#   number = number-1 
# print("Now!")

# ========== 2.3.4 ==========
# password=input("Password: ")
# repeat=input("repeat password: ")
# while True:
#   if password==repeat:
#     break
#   print("They do not match!")
#   repeat=input("repeat password: ")


# print("User account created!")

# ========== 2.3.5 ==========
# pin=int(input("Pin: "))
# tries = 1
# while True:
#     if pin==4321:
#         break
#     print("Wrong")
#     tries = tries+1 
#     pin=int(input("Pin: "))
# print("Correct, it took you", tries, "tries")
# ========== 2.3.6 ==========
# year=int(input("Year:"))
# while True:
#     if year % 4 == 0:
#         print("The next leap year after 2024 is", year)
        


# ========== 2.3.7 ==========
# story = ""
# while True:
#   word=input("Please type in a word: ")
#   if word=="End":
#     break
#   story = story + " " + word

# print(story)

# ========== 2.3.8 ==========
# story= ""
# lastword = ""
# while True:
#     word=input("Please type in a word: ")
#     if word=="end":
#         break
#     if word == lastword:
#         break
#     story= story + " "+ word 
#     lastword = word

# print(story)
# ========== 2.3.9 ==========
count = 0 
sum= 0
mean=0 
positive=0
negative= 0
while True:
    number=int(input("Number: "))
    if number==0:
        break
    count = count + 1
    sum=sum + number 
    mean = sum / count 
    if number >0:
        positive = positive + 1 
    else:
        negative = negative+ 1 
        

    # positive= number> 0
    # negative= number< 0 

print("Numbers typed in: ", count)
print("Sum of numbers:", sum)
print("Mean of numbers: ", mean)
print("Positive numbers: ", positive)
print("Negative numbers: ", negative )