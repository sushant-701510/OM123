#OM SINGH
#23scse1430328


#Q24. Python program to check wether the string is palandrome or not

s = str(input("Enter a string: "))
if s == s[::-1]:
  print("String is palindrome")
else:
  print("String is not a palindrome")