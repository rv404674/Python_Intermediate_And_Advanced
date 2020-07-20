# link 1 - https://realpython.com/lessons/python-generators-overview/
# link 2 - https://realpython.com/introduction-to-python-generators/

# NOTE
small_list = [i for i in range(10)]
big_list = [i for i in range(100000)]

# NOTE: If you are working with some app that uses inf sequence
# then after some time your computer memory wont be able to handle it

"""
Here is when generators come.
Generators allow us to manage these problems one small chunk at a time.
But there is tradeoff between memory and speed.
"""

# NOTE: to make a normal func generator, use "yield"
# to access a gen value, use "next"
# a generator function is remembering where it left off -> it is keeping 
# its state between calls - sort of like bookmark
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

infinite = infinite_sequence()
print(next(infinite)) #0
print(next(infinite)) #1
print(next(infinite)) #2

# TODO:
# When python yield statement is hit, the program suspends function execution and returns the yielded
# value to the caller. (In contrast, return stops function execution completely.)
# When the function is suspended, the state of that function is saved. This includes any variable bindings
# to the local variable, exception handling, internal stack etc.

# what happens when a generator is exhausted
# they will raise 'StopIteration' Expression
def finite_sequence():
    nums = [1,2,3]
    for num in nums:
        yield num

finite = finite_sequence()
print(type(finite))
print(next(finite))
print(next(finite))
print(next(finite))
#print(next(finite))

# NOTE: ANOTHER way to create generator
# generator comprehensions
nums_squared_listcomp = [num**2 for num in range(5)]
# gen comprehension. type = gen
nums_squared_gencomp = (num**2 for num in range(5))


# BENCHMARKING MEMORY
import sys
list_comp = [num**2 for num in range(100000)]
print(sys.getsizeof(list_comp)) #82000bytes
gen_comp = (num**2 for num in range(100000))
print(sys.getsizeof(gen_comp)) #128 bytes

# BENCHMARKING by speed
import cProfile
print(cProfile.run('sum([i**2 for i in range(100000)])')) #0.055

print(cProfile.run('sum((i**2 for i in range(100000)))')) #0.079