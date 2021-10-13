def multiply_list(mylist):
    result = int(1)
    for i in mylist:
        result =int(i) *int(result)
    return result

print(multiply_list([1,2,3,7]))
