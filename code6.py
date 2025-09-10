#NAME OM SINGH,ADMISSION NUMBER 23SCSE1430328
#QUESTION NUMBER-6
#PYTHON PROGRAM TO FIND THE AVERAGE OF A SET OF INTEGERS
numbers=input("enter a set of integers sepaprated by space :") 
numbers_list = [int(num) for num in numbers .spilt()]
sum_numbers=0
for num in numbers_list:
    sum_numbers +=num
    average=sum_numbers/ len(numbers_list)
    print("average", average)