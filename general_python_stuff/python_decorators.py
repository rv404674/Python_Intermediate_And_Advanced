# Decorators add some additional functionality to a function, without chaging the function structure itself.
# NOTE: Read about them in depth

def string_capitalize(function):
    def wrapper():
        func = function()
        string_capitalize = func.upper()
        return string_capitalize
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        split = func.split()
        return split
    return wrapper

@split_string # This is executed second
@string_capitalize # NOTE: THis is executed First.
def hello_world():
    return "hello world"

print(hello_world())


class Address:

    def __init__(self):
        self.name = "Rahul Verma"
        self.age = 22
        self.address = "Kaintha"

temp_address = Address()
print(temp_address.name)