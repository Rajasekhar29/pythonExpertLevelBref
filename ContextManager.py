
# if any of the code get error then it wont work

"""
file = open("file.txt","r")
try:
    file.write("hello")
finally:
    file.close()

"""
# we can slove it using try and expect

# one more way is :-)
"""
with open("file.txt",'r') as file:
    file.write("hello")

"""
# ----------------------------------------------------------------

#  using context manager now
class File:
    def __init__(self,filename,method):
        self.file = open(filename,method)

    def __enter__(self):
        print("Enter")
        return self.file
    
    def __exit__(self,type,value,traceback):
        print(f"{type},{value},{traceback}")
        print("Exit")
        self.file.close()
        # look for sol
        if type == Exception:
            return True
        # return True # here we are telling the python, we are tacktilly handling the exception we can run ,:( be carefull with return true we cant handle all the exception like this one, for that problem we do this.

with File("file.txt",'w') as f:
    print('Middle')
    f.write("Hello!")
    raise FileExistsError()
# we are raiseing an exception still it runs completly

# ----------------------------------------------------------------
#  actually above code looks little bit complex. lests make it easier using contextlib,generator

from contextlib import contextmanager


"""
        This Decorator (@contextlib.contextmanager) turn this generator into a context Manager, it works excatley

"""


@contextlib.contextmanager
def file(filename,method):
    file = open(filename,method)
    yield file
    file.close()
    print('Exit')

with file("text.txt",'w') as f:
    print('middle')
    f.write ("Hello")
