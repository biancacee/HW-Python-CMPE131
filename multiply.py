def multiply_list(mylist):
    result = float(1)
    for i in mylist:
        result =float(i) *float(result)
        result=int(result)
    return result
