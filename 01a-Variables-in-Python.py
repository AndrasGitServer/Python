# Variables in Python   (lesson 01 theory & examples)
#####################################################

# A variable is a name attached to a value (associated)
# which can be changed and used later in the code.

# We use variables to store DATA in the computer's MEMORY.
# Python allocates MEMORY and store the value in that MEMORY SPACE.
# The variable is like a label for that MEMORY LOCATION.
# When we change the "variable" (value of the variable) the MEMORY LOCATION changes !
###################################################################################
# We loose a HANDLE for the previous DATA !
#########################################

# 1. You can change the value of the variable later in your code
#       AND
# 2. During program execution (run-time).

# 3. You can use the name (name-space) instead of the/a value directly in our code.
#    Anywhere in our program to get ACCESS to that MEMORY LOCATION.

# 4. No need of variable DECLARATION before using it.
#    No definition of the TYPE (of data) of the variable.
#    The TYPE of a variable need NOT be specified in advanced.
#    DYNAMIC TYPING = the value of a variable will known at RUN-TIME!

# 5. The names of the variables will be replaced by their values at run-time.

# 6. The variable can store ANY TYPE of value during its lifetime.

# 7. Yes! you need to assign a value (INITIALIZATION = DEFINITION).

x = 10
y = 20
print('x:', x, id(x), '  y:', y, id(y),'  x + y=', x+y)

x = 30
y = 40
print('x:', x, id(x), '  y:', y, id(y),'  x + y=', x+y)

# The next line is NOT allowed!
# print(z)
# Traceback (most recent call last):
# File "/home/megabyte/dir.Python-programs/01-Variables-in-Python.py", line 22, in <module>
# print(z)
#       ^
# NameError: name 'z' is not defined

print()
print('this variable names are NOT a good programming practice:')
_var  = 30
_1var = 40
Var_2 = 50
print(_var + _1var + Var_2)

print()
a = b = c = "This is a STRING variable!"
print(a)
print(b)
print(c)

a, b, c = 1, 2, 3
print(a, b, c)
print(f'a = {a}, b = {b}, c = {c}')
