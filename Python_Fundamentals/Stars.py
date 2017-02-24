def draw_stars(x):
    for num in x:
        ans = ''
        for i in range(num):
            ans += '*'
        print ans
draw_stars([4,6,1,3,5,7,25])

# part two

def draw_starsTwo(x):
    for element in x:
        output = ''
        if type(element) is int:
            for i in range(element):
                output += '*'
        elif type(element) is str:
            firstLetter = element[0].lower()
            for i in range(len(element)):
                output += firstLetter
        print output

draw_starsTwo([4,'Tom',1,'Michael',5,7,'Jimmy Smith'])
