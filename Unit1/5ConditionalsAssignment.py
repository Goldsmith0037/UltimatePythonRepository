
# print("########## 1.5.1 ##########")
# number = int (input*("Please type in a number:"))
# if number == 1984:
#     print("Orwell")
# print("########## 1.5.2 ##########")
# number = int(input("Please type in a number "))
# absolutevalue = number * -1 
# if number < 0:
#     print("The absolute value of this number is", absolutevalue )
# if number > 0: 
#     print("The absolute value of this number is", number )
# print("########## 1.5.3 ##########")
# name= input("What is your name?")
# if name !=("Jerry"):
#     portions= int(input("How many portions of soup?:"))
#     print("The total cost is ", portions * 5.90)
# print ("Next Please!")
# print ("########## 1.5.4 ##########")
# number = int(input( "Type in a number:"))
# if number < 1000:
#     print("This number is smaller than 1000")
# if number < 100:
#     print("This number is smaller than 100 ")
# if number < 10:
#     print("this number is smaller than 10")
# if number > 1000: 
#     print("This number is greater than 1000")
# print("Thank You!")
# print("########## 1.5.5 ##########")
# number1 = int(input ("Number 1:"))
# number2 = int(input("Number 2:"))
# operation = input("Operation:")
# multiply= number1 * number2 
# add = number1 + number2 
# subtract = number1 - number2 
# if operation ==("add"):
#     print( number1, "+", number, "=", add )
# if operation == ("multiply"):
#     print( number1, "*", number2 ,"=", multiply)
# if subtract =="subtract":
#     print(number1, "-", number2, "=", subtract )
# print("########## 1.5.6 ##########")
# tempF = int(input("Type in a temperature (F):"))
# tempC = (tempF- 32) * 5/9
# print ( tempF, "degrees Fahrenhet equals", tempC, "degrees Celsius")
# print("########## 1.5.7 ##########")
# hourlywage = float(input("Hourly wage:"))
# hoursworked = int(input("Hours worked"))
# day= input("Day of the week:")
# dailywages= hourlywage * hoursworked
# dailysunday= dailywages * 2
# if day == ("sunday"):
#     print("Daily wages", dailysunday)
# if day != ("Sunday"):
#     print("Daily wages", dailywages)
print("########## 1.5.8 ##########")
# Fix the program
# points = int(input("How many points are on your card? "))
# points10 = points * 0.1
# pointsbonus10= points10 + points
# points15 = points * 0.15
# pointsbonus15= points15 + points
# if points < 100:
#     print("Your bonus is 10 %")
#     print(" You now have", points10, "points")
# if points > 100:
#     print ("your bonus is 15%")
#     print("You now have", points 15, "points")
print("########## 1.5.9 ##########")
temp = int(input("Temperature:"))
rain = input("Will it rain? (yes/no):")
if temp > (20):
    print("Wear jeans and a T-shirt")
    if rain == ("yes"):
        print ("take a jacket with you and don't forget a umbrella")
        print("I reccommend a sweater as well.")
    if rain == ("yes"):
        print ("Don't forget your umbrella!")
if temp <= (5):
    print("Wear jeans and a T-shirt")
    print("I recommend a sweater as well ")
    print("Take a jacket with you")
    print("I think gloves are in order ")
    if rain == ("yes"):
        print("Don't forget your umbrella!")
        