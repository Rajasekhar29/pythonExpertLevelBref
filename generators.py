

"""
x = [i**2 for i in range(10)]

for el in x:
    print(el)

"""

"""
    
One value at a time, it uses the current memory, with full efficient
it stores one value at a time.
    [extended_summary]
"""


# class Gen:
#     def __init__(self,n):
#         self.n = n
#         self.last = 0
"""
__init__ create
"""    
    # def __next__(self):
    #     return self.next()
"""
        __next__ [it iterates to next element of the given number]

        [extended_summary]
"""
    
    # def next(self):
    #     if self.last == self.n:
    #         raise StopIteration()
"""
        next takes self of its

        [it stops iteration when last and n ==]
        multplies to last ** 2
        then that value stores in another value of rv
        and returns the rv
        Returns:
            [type]: [description]
"""
        # rv = self.last ** 2
        # self.last += 1
        # return rv



# creation of object of Gen(perament of 100)
# g = Gen(100)
# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break
"""
    while loop cuntinues until it comes false
    else iteration become stop it break and comes out of the loop

"""
# ----------------------------------------------------------------
# Converting to  Generator 
# def gen(n):
#     for i in range(n):
#         yield i**2


# g = gen(100000)
# for i in g:
#     print(i)
"""
    gen class taking perameter of n elements
    In the loop touches the yield it puase the function and return the value where it is called.
    it pause's not to stop the function
    We can use many yield we can

"""
# print(next(g))

# ----------------------------------------------------------------
"""
Check out the how much of the memory is used by the generator

"""
import sys

def gen(n):
    for i in range(n):
        yield i**2

x = [i ** 2 for i in range(10000)]
g = gen(10000)

print(sys.getsizeof(x))
print(sys.getsizeof(g))
print(sys.getsizeof("function using with text:",x))
print(sys.getsizeof("gen using with text:",g))
