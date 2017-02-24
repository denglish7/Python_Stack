import random
import math

heads = 0
tails = 0
for count in range(1,5001):
    x = round(random.random())
    if x == 0:
        faceup = 'tail'
        tails+=1
    else:
        faceup = 'head'
        heads+=1
    print "Attempt #"+str(count)+": Throwing a coin...It's a "+faceup+"!...Got "+str(heads)+" head(s) and "+str(tails)+" tail(s) so far"
