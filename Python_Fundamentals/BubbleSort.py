import random

list = []
for i in range(101):
     i = random.random() * 10000
     i = int(round(i))
     list.append(i)


def bubbleSort(list):
    for x in range(len(list)-1, 0, -1):
        for i in range(x):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
bubbleSort(list)
print list
