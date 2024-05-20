# ========== 3.2.1 ==========
string= input("Please type in a string")
amount= int(input("Please type in an amount: "))
word= string * amount
print(word)
========== 3.2.2 ==========
string1= input("Please type in string 1: ")
string2= input("Please type in string 2: ")
if string1 > string2:
    print(string1, "is longer")
else:
    print(string2, "is longer")
# ========== 3.2.3 ==========
string= input("Please type in a string")
position= len(string) - 1
while True:
    print(string[position])
    position= position - 1
    if position== -1:
        break
# ========== 3.2.4 ==========
string=input("Please type in a string: ")
position= len(string) - 1 
if string[1] == string[-2]:
    print("The second and the second to last characters are the same")
else:
    print("The second and the last  characters are different.")
========== 3.2.5 ==========.
width=int(input("Width"))
letter= ("#")
print(width* letter)
# ========== 3.2.6 ==========
+
letter=("#")
height= int(input("Height: "))
num_done= 0
while True:
    print (width*letter)
    num_done= num_done + 1
    if height == num_done:
        break
# ========== 3.2.7 ==========
string=input("Please enter string: ")
print(string)
print("-"*len(string))
# # ========== 3.2.8 ==========
string=input("Please type in a string")
letter="*"
stars= letter * (20 - len(string) ) 
print(stars+ string) 
# ========== 3.2.9 ==========
word=input("Word: ")
stars="*"
print(stars * 30)
leftspaces= float(30- len(word) -2) // 2
rightspaces= float(30 - len(word)- 2)// 2
print("*"+ (leftspaces * " ") + word + (rightspaces * " ") + "*")
print(stars * 30)