#OM SINGH
#23scse1430328

#Q20. Python program to implement linear search
l = [2,5,7,11,14,20,22]
x = int(input("Enter the number to be searched: "))
for i in range(len(l)):
    if l[i] == x:
        print("Element found at index " + str(i))
        break
else:
  print("Elment not found")