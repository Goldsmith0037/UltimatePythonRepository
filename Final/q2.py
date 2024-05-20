number=50
insert= int(input("Insert Coin:"))
import time
time.sleep(1)
while True:
     time.sleep(1)
     number = number - insert
     print(number)
     if number == 25:
          print("amount due:",number )
          break
insert= int(input("Insert Coin: "))
if number == 0:
     print(" Change owed 0")
     
    # How close was I to figuring this out