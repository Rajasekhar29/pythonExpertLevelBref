#----------------------------------------------------------------
# it is type class
def hello():

    class Hi():
        pass
    return Hi
"""
Meta class defines how the 'Hi' class is created and operated.
Meta class create the rules for a class
[extended_summary]
"""
#----------------------------------------------------------------

class Test():
    pass
    """
    Test This class it self an object, think like object is created,
    who created this object that is also an object it is called Meta class
    [extended_summary]

    type(class) is ?
    it is class <type> .

    <class '__main__.Test'>
    <class 'type'>
    """

print(Test)
print(type(Test))

#----------------------------------------------------------------
"""
Below code simmiler to creating the Class with out using class keyword in Python
this is the power of Python
<__main__.Test object at 0x7f8931a7eb20>
<class 'type'>

Here is the proof of it..:)

"""

Test = type('Test',(),{})
print(Test())
print(type(Test))

#----------------------------------------------------------------


Test = type('Test',(),{"x":5})
t = Test()
print(t.x)

"""
check out the we perform operation here
"""
#----------------------------------------------------------------
# Inheritince
class Mother:
    def home(self):
        return('hi')

Test = type('Test',(Mother,),{"x":5})
t = Test()
print(t.home())

#----------------------------------------------------------------
# Methods
class Mother1:
    def home(self):
        return('hi')
def add_attribute(self):
    self.z = 9

Test = type('Test',(Mother1,),{"x":5,"add_attribute":add_attribute })

t = Test()
t.add_attribute()
print(t.z)
#----------------------------------------------------------------
# Remember meta class lies aboue your class





class Meta(type):
    """
    Meta class always inherts the type object

    [extended_summary]

    Args:
        type ([objcet]): [it is hinheritence]
    """
    def __new__(self,class_name,bases,attrs):
        """
        __new__ method
        obj constructed after this 
        [it is called before the __init__ method]
        """
        print(attrs)

# changing the small letter casses to uper letter
        a = {}
        for name,val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
            
        print(a)
        return (type(class_name,bases,attrs))
    

class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print('Hai')
 
"""
    i am not calling the Dog class but still it is printing
    it is for meta class

"""
d= Dog()
print(d.X)

# for your reference you are not going to use it in your programmig, it is just for our understand, How class and object work
# for more check out the documentation : https://docs.python.org/3/reference/datamodel.html#customizing-class-creation


