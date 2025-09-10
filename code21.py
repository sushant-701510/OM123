#OM SINGH
#23scse1430328

#Q21. Python program to implement binary search

l = [2,5,7,11,14,20] 
x = int(input("Enter the number to be searched: "))
low = 0
high = len(l)-1
mid = 0
while low <= high:
    mid = (high + low) // 2
    if l[mid] < x:
        low = mid + 1
    elif l[mid] > x:
        high = mid - 1
    else:
        print(mid)
        break
if x not in l:
  (print("Element not found"))
