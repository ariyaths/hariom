
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"wrapper_function ran before {original_function.__name__} "
               f"function")
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print('display function ran')

display()


@decorator_function
def display_name(name, age):
    print(f"displaying the name {name} and age {age} from display_name "
          f"function")


display_name("John", 23)
