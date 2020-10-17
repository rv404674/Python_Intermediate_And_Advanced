# Video - https://www.youtube.com/watch?v=eqoy0iwUAA4&ab_channel=InterviewBit

# Example
# values = []
# for i in range(100000):
#     .....
#     print(i)

# but what happens is, at a certain value, the program pauses
# let say at 1490
# ...
# ... smoothly runs
# ....
# then again at 45000
# ....

# If we are working on a producer/consumer problem, in the consumer side, and if the consumer pauses
# the queue may overflow. We dont want that

# NOTE: This is caused by Python's GC.

## NOTE: How Python's GC Works

c/c++ = Manual Memory Mangement
int arr[10] -> stack
int *arr;
arr = malloc(**) -> HEAP

C++ will not clear the memory allocated in the heap automatically. If we forget to clear it, it will cause
memory leaks.

SO basically Manual Memory Management is Tedious and bug prone.

### Programmer Friendly Languages

Java, Python, JS
Automatic GC, they try to handle the task of freeing memory for you.

l = list(range(10000))
del l # NOTE: This wont delete the memory allocated to l. It will just ubind local variable l from the mem location


x = 10 # memory = 10245
# y might be pointing to same mem location.
import sys
print(sys.getrefcount(x))
# 161
# NOTE:
# It basically tells you how many different variables in python code are referencing to same memory location.
# WHy 161 -> python keeps a cache for small numbers.

y = "hello rahul verma"
print(sys.getrefcount(y))
# 2
# Two references one from y, and one from the param that is passed in getrefcount.


#NOTE:
# Python's Garbage Collection is a Reference Counting GC.
# It keeps track of number of variables that are referring to a particular mem location. If the count becomes zero, it frees up the memory.

l = [1,2,3]
l.append(l)
# l = [1,2,3, [1,2,3]]
# now even if you delete l, the reference from list inside wont get deleted, problem
# TO handle this, Python's GC, after some interval, it will go over all variables and see which are reachable.

# It is basically a memory graph.


