#!/usr/bin/env python

import random

ulim = 10000000000
llim = 0

a = random.randint(llim,ulim)


upper = ulim
lower = llim

guess = int((upper+lower)/2)

print a
print "\n\n"
#print guess
print "guess\tupper\tlower"
print "%i\t%i\t%i\t%i" % (guess, upper, lower,a)

while (True):
    if (guess == a):
        print "FOUND!\t", guess
        break
    elif (guess > a):
        upper = guess 
        guess = int((upper+lower)/2)
        print "%i\t%i\t%i\t%i" % (guess, upper, lower,a)
    elif (guess < a):
        lower = guess
        guess = int((upper+lower)/2)
        print "%i\t%i\t%i\t%i" % (guess, upper, lower,a)
        #print "New guess:\t", guess
    else:
        continue




