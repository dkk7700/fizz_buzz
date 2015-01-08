#!/usr/bin/env python
import sys

# default value of n
n = 21

arg_len = len(sys.argv)

if arg_len == 1:
    while(True):
        n_in = raw_input("Please enter an integer: ")
        try:
            n = int(n_in)
            break
        except:
            print "%s is not an integer. Please try again." % (n_in)
elif arg_len >= 2:
    try:
        n = int(sys.argv[1])
    except:
        print "%s is not an integer. Setting n to the default: %s" % (str(sys.argv[1]), str(n))
else:
    pass

print "Fizz buzz counting up to %i" % n

for i in range(1,n+1):
    if ((i % 3 ==0) and (i % 5 == 0)):
        print "fizz buzz"
    elif (i % 3 == 0):
        print "fizz"
    elif (i % 5 == 0):
        print "buzz"
    else:
        print i
