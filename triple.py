def tripler(func):
    def wrapper_tripler():
        """A decorator that can be used in other functions. This decorator
           is passed a function and contains a nested function which calls            the function that is passed three times.
        """
        func()
        func()
        func()
    return wrapper_tripler
