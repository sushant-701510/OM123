#OM SINGH
#23scse1430328

#Q22. Python program to find the largest number in a list withoiut using Built-in-functions,

lst = [11, 7, 14, 9, 5]
max_num = lst[0]
for n in lst:
    if n > max_num:
        max_num = n
print(max_num)