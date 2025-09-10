# OM SINGH 
#23SCSE1430328

#Q16.Python program to check wether the given integer is a prime number or not.

a=int(input("enter a number:"))
if a < 2:
    print(a, "is not a prime number")
else:
    for i in range(2, a):
        if a % i == 0:
          print(a, "is not a prime number")
          break
    else: 
       print(a, "is a prime number")