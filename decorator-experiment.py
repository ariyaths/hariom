
from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log',
                        level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args}, and kwargs {kwargs}')
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in {t2} sec')
        return result

    return wrapper


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


@my_logger
@my_timer
def display_name(name, age):
    print(f"displaying the name {name} and age {age} from display_name "
          f"function")


display_name("John", 23)


# *** Second part of the learning ***
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@gmail.com"

    def fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Hari', 'Om', 60000)

print(emp_1)
print(emp_2)

print(emp_1.fullname)
print(emp_1.fullname())

