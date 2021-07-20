#############
# Variables #
#############
course_name = """ 
Multiple
Lines
"""
x, y = 1, 2
x = y = 1

###################
# Type Annotation #
###################
age: int = 20  # need to select linter called "mypy" to get errors if you
# want to specify a type for a variable this way
age = "Python"

###############################
# Mutable and Immutable Types #
###############################
x = 1  # ints are immutable --> memory space allocated for each assignment to an int
print(id(x))
x = 2  # this 'x' has a different memory address
print(id(x))
# lists are mutable --> same memory space even if you change contents of list
x = [1, 2, 3]
print(id(x))
x.append(4)  # has same memory address
print(id(x))

####################
# Escape Sequences #
####################
m = 'Python "Programming'
print(m)
m = "Python \"Programming"
print(m)
m = "Python \\Programming"
print(m)
m = """Python
Programming"""
print(m)
# Also have : \"   \'   \\   \n

#####################
# Formatted Strings #
#####################
first = "Cathleen"
last = "Pena"
full = first + " " + last
print(full)
last = "Gutierrez"
print(full)
# ---------------------------
first = "Cathleen"
last = "Pena"
# formatting allows you to call those variables at run time
full = f"{first} {last}"
print(full)
full = f"{len(first)} + {4 + 4}"
print(full)

##################
# String Methods #
##################
c = "  PytHon Programming"
print(c.title())
print(c.strip())  # also lstrip, rstrip
print(c.find('PRo'))  # returns start index of found expression, -1 if not found
print(c.replace('P', '-'))
print("Programming" in c)
print("Programming" not in c)

###########
# Numbers #
###########
x = 2
x = 0b10  # binary representation of 2
print(x)
x = 2
print(bin(x))  # bin() function get you the binary rep of that #
x = 0x12c  # hexidecimal format
print(f"decimal format: \t\t\t{x}")  # will give it to you in decimal format
# will give it to you in hexidecimal format
print(f"hexidecimal format: \thex(x)")

# Imaginary numbers
x = 2 + 3j
print(x)

##############
# Conditions #
##############

age = 12
m = ''

if age >= 18:
    m = 'eligible'
else:
    m = 'not eligible'
print(m)

# more compact way...
m = 'eligible' if age >= 18 else 'not eligible'
print(m)

############
# For Else #
############
names = "Cathleen", "Bella"
for name in names:
    if name.startswith("K"):
        print("found")
        break
else:
    print("not found")

#############
# Functions #
#############
def increment(number:int, by:int = 1) -> tuple:
    return (number, number + by)
print(increment(2, by=5))

def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total
print(multiply(1, 2, 3, 4))

def save_user(**user):
    print(user['name'])
    return user #returns dict of kwargs
print(save_user(id=1, name='admin'))

print("start")
print(multiply(1, 2, 3, 4))
print("finish")

def fizzbuzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return input
print(fizzbuzz(7))