# NOTE: 1. They pollute your name space 
def randint():
    # returns something based ona dice throw
    pass

from random import *

randint()
# error :
# randint() got overwritten by randint() from random

# NOTE: 2. Difficult to understand where is the function called from
from random import *
values = [1,2,3,4,5]

.....
....
... 1000 lines...

# it becomes difficult to find that choice came from random.
print(choice(values))
