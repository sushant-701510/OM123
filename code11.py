#NAME OM SINGH,ADMISSION NUMBER 23SCSE1430328
#QUESTION NUMBER-11
#PYTHON PROGRAM TO FIND  THE AVERAGE OF 10 NUMBERS USING WHILE LOOP.
total=0
count=0
while count<10:
    number=int(input("enter a number:"))
    total +=number
    count +=1
    average=total/10
    print("averge of 10 numbers are:",average)