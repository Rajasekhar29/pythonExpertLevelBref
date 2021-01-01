"""
  Decorators is used to change the behaiour of the function with out changing the code in it.


    [extended_summary]
"""
def func(string):
    def wrapper():
        print("Started")
        print(string)
        print("Ended")
    return wrapper() 
    # return wrapper # {}


x = func("Hello")

"""
# Enable after uncommenting above wrapper
print(x)
x()
"""

# ----------------------------------------------------------------
def func(f):
    def wrapper():
        print("Started")
        f()
        print("Ended")
    return wrapper() 
    # return wrapper # {}

def func2():
    print("I am func2")

def func3():
    print('i am func3')

x = func(func2)
print(x)
# x()

x = func(func3)
y = func(func2)
print(x)
# x()
# y()

#----------------------------------------------------------------
# function calling using simple one line
def func(f):
    def wrapper():
        print("Started")
        f()
        print("Ended")
    return wrapper() 
    # return wrapper # {}

def func2():
    print("I am func2")

def func3():
    print('i am func3')


func3 = func(func3)
func2 = func(func2)
func3()
func2()

# ----------------------------------------------------------------

#----------------------------------------------------------------
# using decorators
def func(f):
    def wrapper(x):
        print("Started")
        f(x)
        print("Ended")
    return wrapper() 
    # return wrapper # {}
@func
def func2(x):
    print("I am func2")
@func
def func3():
    print('i am func3')

func2()
func3()
# ----------------------------------------------------------------

"""
     
     if we want to gave a parametersied arguments that case it gaves error as
     to over come from this poblem we have unpack operator(*args, **kwargs)

    [extended_summary]
"""

def func(f):
    def wrapper(*args,**kwargs):
        print("Started")
        f(*args,**kwargs)
        print("Ended")
    return wrapper() 


@func
def func2(x):
    print("I am func2")
@func
def func3():
    print('i am func3')

func3()
func2(5,6)
#----------------------------------------------------------------
"""
     One more problem when we want to retrun an argument then we get a problem
     How can we solve this problem.?
     Ans: store the args&kwargs value into the new variable and retrun it like this 

    [extended_summary]
"""
def func(f):
    def wrapper(*args,**kwargs):
        print("Started")
        rv = f(*args,**kwargs)
        print("Ended")
        return rv
    return wrapper() 
@func
def func2(x):
    print("I am func2")
@func
def func3():
    print('i am func3')


x = func2(5,6)
print(x)








# ----------------------------------------------------------------
# Example 1 timmer decorator
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("Time:",total)
        return rv
    return wrapper

@timer
def test():
    for _ in range(1000):
        pass



@timer
def test2():
    time.sleep(2)


test()
test2()

