#OM SINGH
#23scse1430328

#Q17. Python program to find the roots of a quadratic equation.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

d = (b*2 - 4*a*c)*0.5
root1 = (-b + d) / (2 * a)
root2 = (-b - d) / (2 * a)
print("The roots are:", root1, "and", root2)