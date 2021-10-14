mylist=[]

def multiply_list(mylist):
    """This function takes a list and multiplies the elements within the list. Upon completion the function returns the result of the multiplies elements in the list.
    """
    result=1 
    for i in mylist:
        result = i * result #takes each elemnts and multiplies
    return result

