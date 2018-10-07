import time
import math
import pandas

def printStatements1():
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

def myInputTests():
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
    #harihara.nair@gmail.com
    #slice the name from the input email
    username = email[:email.index("@"):]
    domain = email[email.index("@") + 1:email.index(".com"):]
    #print info of user
    print("Hey your name is {} and your email domain is {}".format(username, domain));time.sleep(0.1)

def printStatements2():
    #booleaning
    print(True);time.sleep(0.1)
    print(False);time.sleep(0.1)
    a = True
    print("a = ",True);time.sleep(0.1)
    print("type (a)",type (a));time.sleep(0.1)
    a2 = "True"
    print('a2 = "True"');time.sleep(0.1)
    print("type (a2) = ",type (a2));time.sleep(0.1)
    print("3 > 4 = ",3 > 4);time.sleep(0.1)
    print("4 > 3 = ",4 > 3);time.sleep(0.1)
    print("3 == 4 = ",3 == 4);time.sleep(0.1)
    print("45 != 4 = ",45 != 4);time.sleep(0.1)
    print("3 <= 4 = ",3 <= 4);time.sleep(0.1)
    #if and else commands
    num1 = 2
    num2 = 3
    if num1 < num2:
        print("num1 is smaller");time.sleep(0.1)
    else :
        print("num2 is smaller");time.sleep(0.1)
    weather = "Sunny"
    if (weather == "Sunny"):
        print("weather is pleasant");time.sleep(0.1)
        print("it is a bit hot outside");time.sleep(0.1)
        print("feels like a good time to go to a sandy beach and have fun");time.sleep(0.1)
    elif (weather == "Winter"):
        print("weather is unpleasant");time.sleep(0.1)
        print("it is a lot cold outside");time.sleep(0.1)
        print("feels like a good time to go outside and play snowball fights");time.sleep(0.1)
    else :
        print("uknown");time.sleep(0.1)

def video14video16(x,y):
    # #video14
    not True
    not False
    #x = 3
    #y = 4
    if not x > y:
        print("it worked");time.sleep(0.1)
    num3 = 3
    num4 = 4
    num5 = 1
    if (bool(num3 > 7) ^ bool(num4 == 4)):
        print("it is true");time.sleep(0.1)
    else: 
        print("it is false");time.sleep(0.1)
    # #video15
    while num5 <= 10:
        print("legends of awesomeness");time.sleep(0.1)
        print("sweet!");time.sleep(0.1)
        num5 += 1
    L = []
    while(len(L) < 3):
        new_name = input("What is your name?").strip().capitalize()
        L.append(new_name)
    print(L);time.sleep(0.1)
    print ("list is full");time.sleep(0.1)
    # #video16
    for i in range(5):
        print(i)
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(i)

def video17video19():
    # #video17
    our_list = [1, 4, 5, 3, 53, 4]
    print("our_list = ", our_list, "\n");time.sleep(0.1)
    new_list = ["A", "B", "C", 1, 2, 3, 4, True, False]
    print("new_list = ", new_list, "\n");time.sleep(0.1)
    print("new_list[3] = ", new_list[3]);time.sleep(0.1)
    print("new_list[6] = ", new_list[6]);time.sleep(0.1)
    print("new_list[-3] = ", new_list[-3]);time.sleep(0.1)
    print("new_list[3:6:] = ", new_list[3:6:]);time.sleep(0.1)
    print("new_list[3:6] = ", new_list[3:6]);time.sleep(0.1)
    print("new_list[3:] = ", new_list[3:]);time.sleep(0.1)
    print("new_list[6::] = ", new_list[6::], "\n");time.sleep(0.1)
    our_list2 = [1, 2, [3, 4, 5], [6, 7]]
    print("our_list2[2] = ", our_list2[2]);time.sleep(0.1)
    print("our_list2[2][1] = ", our_list2[2][1]);time.sleep(0.1)
    print("our_list2[3][1] = ", our_list2[3][1]);time.sleep(0.1)
    print('our_list2.append("new item") = ', our_list2.append("new item"));time.sleep(0.1)
    print("our_list2 = ", our_list2);time.sleep(0.1)
    print("our_list2.pop() = ", our_list2.pop());time.sleep(0.1)
    print("our_list2 = ", our_list2);time.sleep(0.1)
    print("our_list2.pop(1) = ", our_list2.pop(1));time.sleep(0.1)
    print("our_list2 = ", our_list2);time.sleep(0.1)
    print("len(our_list2) = ", len(our_list2), "\n");time.sleep(0.1)
    # #video18
    employee = {}
    print("employee = ", employee);time.sleep(0.1)
    employees = {
        "Mary" : 24,
        "Gru" : 40,
        "Dan" : 43,
        "Ciara" : 30
    }
    print("employees = ", employees);time.sleep(0.1)
    print('employees["Marry"] = ', employees["Mary"]);time.sleep(0.1)
    print("employees['Ciara'] = ", employees['Ciara']);time.sleep(0.1)
    employees['Ham'] = 23
    print("employees = ", employees);time.sleep(0.1)
    employees['Gru'] = 41
    print("employees = ", employees);time.sleep(0.1)
    del employees['Dan']
    print("employees = ", employees);time.sleep(0.1)
    print("employees.keys() = ", employees.keys());time.sleep(0.1)
    a = list(employees.keys())
    print("a = ", a);time.sleep(0.1)
    print("a[0] = ", a[0]);time.sleep(0.1)
    print("employees.values() = ", employees.values());time.sleep(0.1)
    print("employees.items() = ", employees.items());time.sleep(0.1)
    # #video19
    dic = {}
    s = input()
    for s in s:
        dic[s] = dic.get(s, 0) + 1
    print("\n" .join(['%s,%s' %(k,v) for k,v in dic.items()]))

def video20video22():
    # #video20
    def add(x,y):
        return x + y
    x = add(x = 5, y = 6)
    print(x);time.sleep(0.1)
    def rev(text):
        print(text[::-1]);time.sleep(0.1)
    rev("Harihara and Omkar")
    # #video21
    def info(name, age, likes = "java"):
        detail = "I am {}. I am {} years old and I like {}.".format(name, age, likes)
        print("detail = ", detail)
    info("Harihara", 11, "python")
    # #video22
    ###very important chapter
    ###must for making a game
    print("1, 2, 3, 4, 5 = ", 1, 2, 3, 4, 5)
    number2 = [1, 2, 3, 4, 5]
    print("number2 = ", number2)
    print("*number2 = ", *number2)
    print(("number2 = ", number2))
    def add2(*num):
        total = 0
        for numb in num:
            total += numb
        return total
    print(add2(9, 8, 7, 6, 5, 4, 3, 2, 1, 987654321, 1234567890))
    def about(**kwargs):
        for key,value in kwargs.items():
            print("{} is {}".format(key,value))
    about(Python = "Easy", Java = "Difficult")
    print([ (a, b) for a in range(3) for b in range(a) ])

def stuffIfound():
    ###found from google python
    print("Found this stuff from google python");time.sleep(0.1)
    xyz = [5, 1, 4, 3]
    print("xyz = ", xyz);time.sleep(0.1)
    print("sorted(xyz) = ", sorted(xyz));time.sleep(0.1)
    strs = ['aa', 'BB', 'zz', 'CC']
    print ("sorted(strs) = ", sorted(strs));time.sleep(0.1) ##(case sensitive)
    print ("sorted(strs, reverse = True) = ", sorted(strs, reverse = True));time.sleep(0.1)
    strs2 = ['ccc', 'aaaa', 'd', 'bb']
    print ("sorted(strs2, key = len) = ", sorted(strs2, key = len));time.sleep(0.1)
    ## "key" argument specifying str.lower function to use for sorting
    print ("sorted(strs2, key = str.lower) = ", sorted(strs2, key = str.lower));time.sleep(0.1)
    ## Say we have a list of strings we want to sort by the last letter of the string.
    strs3 = ['xc', 'zb', 'yd' ,'wa']
    ## Write a little function that takes a string, and returns its last letter.
    ## This will be the key function (takes in 1 value, returns 1 value).
    def MyFn(s):
        return s[-1]
    ## Now pass key=MyFn to sorted() to sort by the last letter:
    print ("sorted(strs3, key = MyFn) = ", sorted(strs3, key = MyFn));time.sleep(0.1)

#printStatements1()
#myInputTests()
#printStatements2()
#video14video16(3,4)
#video17video19()
#video20video22()
stuffIfound()