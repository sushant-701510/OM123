#NAME OM SINGH,ADMISSION NUMBER 23SCSE1430328
#QUESTION NUMBER-5
#PYTHON PROGRAM TO DISPLAY THE SUM OF IN NUMBERS USING A LIST
sum=0
print("enter the value of n:")
n=int(input())
print("enter"+ str(n)+ "numbers:")
for i in range(n):
    num=int(input())
    sum=sum + num
    print("sum of" + str(n) + "numbers=" +str(sum))