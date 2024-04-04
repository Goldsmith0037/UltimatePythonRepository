print("########## 1.4.1 ##########")
number = int (input("Please type a number:"))
product = number * (5) 
print (number  ,"times", 5 ,"is " ,product)
print("########## 1.4.2 ##########")
name = (input( "what's your name "))
year = int (input("Which year were you born?"))
print ("Hi,", name, ",you will be ",2024 - year, "years old at the end of the year")
print("########## 1.4.3 ##########")
days = int( input("How many days?"))
print( "Seconds in that many days", days * 86400)
print("########## 1.4.4 ##########")
#
numberf = int(input("Please type in the first number: "))
numbers = int(input("Please type in the second number: "))
numbert = int(input("Please type in the third number: "))

product= numberf * numbers * numbert

print("The product is", product)

print("########## 1.4.5 ##########")
numberf = int(input("Number 1:"))
numbers = int(input("Number 2:"))
sum= numberf, + numbers 
product = numberf * numbers 
print ( "the sum of the numbers", sum)
print ( "The product of the numbers:", product )
print("########## 1.4.6 ##########")
number1 = int(input( "Number 1:"))
number2 = int(input( "Number 2:"))
number3 = int(input( "Number 3:"))
number4 = int(input( "Number 4:"))
sum = number1 + number2 + number3 + number4
mean = sum / 4.00
print ( " The sum of the numbers is", sum,  "and the mean is ", mean) 
print("########## 1.4.7 ##########")
number1 = float(input("How many times a week do you eat at the student cafeteria?:"))
number2 = float(input("The price of a typical student lunch?:" ))
number3 = float(input( "How much money do you spend on groceries in a week?:"))
lunchtotal= number1 * number2 
total= lunchtotal + number3 
daily = total / 7 
print( "average food expenditure")
print("Daily:", daily )
print ("weekly", total )
print("########## 1.4.8 ##########")
students= int (input ("How many students on the course?"))
size = int( input("Desired group size:"))
number= students // size 
print("number of groups formed:", number )