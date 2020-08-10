#NOTE: Identifiers

# \d - number
# \D - anything but not a number
# \s - space
# \S - anything but not a space
# \w - any character
# \W - anything but not a character
# . = any character, except for a new line
# \b - whitespace around word
# \. - a period

# NOTE: Modifier
# {1,3} - we are expecting 1-3
# + - Match 1 or more
# ? - Match 0 or 1
# * - Match 0 or more
# $ - match the end of string
# ^ - match the beginning of the string
# | - either or
# [] - range or "variance" [1-5a-qA-Z]
# {x} - expecting "x" amount

# # NOTE: white space char
# \n - new line
# \s - space
# \t - tab

import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar is 102.
'''

# pull and the name and age

ages = re.findall(r'\d{1,3}', exampleString)
#Out[5]: ['15', '27', '97', '102']

name = re.findall(r'[A-Z][a-z]*', exampleString)
#Out[7]: ['Jessica', 'Daniel', 'Edward', 'Oscar']
