import time
import math

print('hello world');time.sleep(0.1)
print('print(11 + 2) = ', 11 + 2);time.sleep(0.1)
print('print(11 - 2) = ', 11 - 2);time.sleep(0.1)
print('print(11 * 2) = ', 11 * 2);time.sleep(0.1)
print('print(11 / 2) = ', 11 / 2);time.sleep(0.1)
print('print(11 % 2) = ', 11 % 2);time.sleep(0.1)
print('print(11 ** 2) = ', 11 ** 2);time.sleep(0.1)
print('print(11 // 2) = ', 11 // 2);time.sleep(0.1)
print('math.ceil(2.888888) = ',math.ceil(2.888888));time.sleep(0.1)
print('math.floor(2.888888) = ',math.floor(2.888888));time.sleep(0.1)
print('math.pow(2,3) = ',math.pow(2,3));time.sleep(0.1)
print('math.pi = ',math.pi);time.sleep(0.1)
print('math.tau = ',math.tau);time.sleep(0.1)
print('tom said to me that,"i will see you later"');time.sleep(0.1)
print("hi i am {}".format("name"));time.sleep(0.1)
print('"Happy Birthday".count("a")'"Happy Birthday".count("a"));time.sleep(0.1)
x = "Happy Birthday"
print('x.lower() = ',x.lower());time.sleep(0.1)
print('x = ',x);time.sleep(0.1)
x = x.lower()
print('x,x.upper() = ', x,x.upper());time.sleep(0.1)
print('x.capitalize() = ',x.capitalize());time.sleep(0.1)
print('x.title() = ',x.title());time.sleep(0.1)
print('x.islower() = ',x.islower());time.sleep(0.1)
print('x.isupper() = ',x.isupper());time.sleep(0.1)
print('x.isalpha() = ',x.isalpha());time.sleep(0.1)
print('"qwerty".isalpha() = ',"qwerty".isalpha());time.sleep(0.1)
print('"1234".isdigit() = ',"1234".isdigit());time.sleep(0.1)
x = "bohemian"
print('x.index("o") = ',x.index("o"));time.sleep(0.1)
print('x.find("rjufrufur") = ',x.find('rjufrufur'));time.sleep(0.1)
print('x.find("O") = ',x.find("O"));time.sleep(0.1)
print('x.find("o") = ',x.find("o"));time.sleep(0.1)
name = input("What is your name?")
print('len(name) = ',len(name));time.sleep(0.1)
name = input("What is your name?").strip()
print('len(name) = ',len(name));time.sleep(0.1)
name2 = input("What is your name ?")
age = 46
print("Your name is {} and age is {}".format(name2, age))

name3 = input("What is your name ?")
age2 = input("What is your age ?")
size = input("What is your size?")
colour = input("What is your favourite colour?")
animal = input("What is your favourite animal?")
number = input("What is your favourite number?")    
print("Your name is {}, age is {}, size is {}, favourite colour is {}, favourite animal is {} \
and favourite number is {}".format(name3, age2, size, colour, animal, number));time.sleep(0.1)
#slicing
info = "hi i am a compter engineer"
print(info[10:18:]);time.sleep(0.1)
var = "hello"
print(var[::-1]);time.sleep(0.1)
#input the email of user
email = input("enter your email ID ?")
#siddhant4000@gmail.com
#slice the name from the input email
username = email[:email.index("@"):]
domain = email[email.index("@") + 1:email.index(".com"):]
#print info of user
print("Hey your name is {} and your email domain is {}".format(username, domain));time.sleep(0.1)

