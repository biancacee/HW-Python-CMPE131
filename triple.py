def tripler(func):
    def wrapper_tripler():
        func()
        func()
        func()
    return wrapper_tripler
