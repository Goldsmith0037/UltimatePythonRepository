# ========== 4.2.1 ==========
# def greatest_number(number1, number2, number3):
#     if number1 > number2 and number1 > number3:
#         return(number1)
#     elif number2 > number1 and number2> number3:
#         return (number2)
#     else:
#         return(number3)
# print(greatest_number(3, 4, 1))
# print(greatest_number(99, -4, 7))
# print(greatest_number(0,0,0))
# ========== 4.2.2 ==========
def same_chars(word,index1,index2):
    if index1 > len(word) or index2 > len(word):
        return("the second index is not within the string")
    

    letter1= word[index1]
    letter2 =word[index2]


    if letter1 ==letter2:
        return("True")
    elif index1 > len(word) or index2 > len(word):
        return("the second index is not within the string")
    else:
        return("False")
    
print(same_chars("programmer", 6, 7))
print(same_chars("programmer", 0, 4))
print(same_chars("programmer", 0, 12))
# ========== 4.2.3 ==========


