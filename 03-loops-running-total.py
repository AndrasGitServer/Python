'''
Python for Everybody - Full University Python Course
freeCodeCamp.org
py4e.com
Dr. Chuck

Chapter 5   Loops & Iteration
            Repeated Steps

Time in the video 2 hours: 15 min.

INDEFINITE LOOPS  ->  use the WHILE keyword.
because they keep going until a logical condition becomes False
You have to check the ITERATION VARIABLE to get out of the loop.

DEFINITE LOOP  ->  use the FOR and IN keyword (construct).
it is going to loop through soem set of things (a list of items)
(a finite set) of things.
They execute an exact number of times.

The for loop includes a mechanism to construct the iteration variable for us!

'''


n = 3           # n is the Iteration Variable, tells how many times to run the loop
while n > 0 :
    print(n)
    n = n - 1
print('while loop finished, did the indented block 3 times (3x)', '\n')


# ZERO-TRIP loop
n = 0
while n > 0 :
    print('ZERO-TRIP loop')
print('ZERO-TRIP loop :-)', '\n')


# break is a LOOP CONTROL STATEMENT
while True :
    line = input('> ')
    if line == 'q' :
        break
    print(line)
print('q pressed -> BREAK OF OF THE LOOP\n')


# continue is also a LOOP CONTROL STATEMENT
while True :
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'q' :
        break
    print(line)
print('q pressed, did you press # -> CONTINUE in the loop\n')


for i in [1,3,5,7,9] :
        if i==1 :
            count = 0
            total = 0
        count += 1
        total += i              # RUNNING TOTAL is running in the loop
        print(i, count, total)

