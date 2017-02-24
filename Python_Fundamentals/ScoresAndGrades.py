from random import randint
for count in range(1,10):
        x = randint(60, 100)
        if x < 69:
            print "Score: " + str(x) + "; Your grade is a D"
        elif x < 79:
            print "Score: " + str(x) + "; Your grade is a C"
        elif x < 89:
            print "Score: " + str(x) + "; Your grade is a B"
        else:
            print "Score: " + str(x) + "; Your grade is a A"
