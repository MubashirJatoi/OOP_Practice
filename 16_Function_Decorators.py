def log_function_call(func):
    def Wrapper():
        print("Function is being called")
        return func()
    return Wrapper        

@log_function_call
def say_hello():
    print("hello.")

say_hello()