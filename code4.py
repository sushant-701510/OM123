#NAME OM SINGH,ADMISSION NUMBER 23SCSE1430328
#QUESTION NUMBER-4
#PYTHON PROGRAM TO FIND THE GEOMETRIC MEAN OF IN NUMBERS.
n=int(input("enter the number of elements:"))
numbers=[]
for i in range (n):
    num=float(input(f"enter number{i +1}:"))
    numbers.append(num)
    product=1
    for num in numbers:
        product*=num
        geometric_mean=product**(1/n)
        print("the geometric mean of the number is :", geometric_mean)