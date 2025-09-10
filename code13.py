#NAME OM SINGH,ADMISSION NUMBER 23SCSE1430328
#QUESTION NUMBER-13
#PYTHON PROGRAM TO FIND THE SUM OF THE DIGITS OF THE GIVEN INTEGER USING WHILE LOOP.
a=int(input("enter an integer"))
s=0
while a>0:
    d=a%10
    s=s+d
    a=a//10
    print("sum of digits is:",s)