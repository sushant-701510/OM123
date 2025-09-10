#NAME OM SINGH,ADMISSION NUMBER 23SCSE1430328
#QUESTION NUMBER-8
#PYTHON PROGRAM TO FIND THE PRODUCT OF A SET OF REAL NUMBERS.
a=int(input("enter the numberof elements:"))
numbers=[]
for i in range(a):
    num=float(input("enter number{}:".format(i+1)))
    numbers.append(num)
    product=1
    for num in numbers:
        product*=num
        print("the product of the number is:"+str(product))