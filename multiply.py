def multiply_list(mylist):
    result = 1
    for i in mylist:
        result = int(i)* result
    return result

print(multiply_list([1,2,3,7]))
