def function1(function):
    def wrapper():
        print("Hello")
        function()
        print("Welcome to Python Edureka Tutorial.")
    return wrapper

def function2():
    print("Pythonista")

func2=function1(function2)
func2()