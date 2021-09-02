import math, os, random, re, sys, string, itertools, collections
from collections import *

def p():
    T = int( input() )
    for t in range(T):
        S, E = ( int(s) for s in input().split())
        seen = set()
        
        arr = [ int(s) for s in input().split() ]
        sol = []
        for x in arr:
            if x in seen:
                sol.append(S-x)
                sol.append(x)
                break
            else:
                seen.add( S - x )
                
        if len(sol) > 0:
            if sol[0] < sol[1]:
                print( sol[0], sol[1] )
            else:
                print( sol[1], sol[0] )
        else:
            print("!OK")

#p()
arr = [1,3,4,5]
if (1 in arr):
    print('si')



