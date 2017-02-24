def multiply(a,x):
    for i in range(len(a)):
        a[i] = a[i] * x
    return a

print multiply([2,4,10,16], 5)
