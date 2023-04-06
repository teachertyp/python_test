fizz = int(input())
buzz = int(input())
t = int(input())
for i in range(1,t+1):
    if i == 1:
        print(i,"", end='')
    elif i % fizz == 0 and i % buzz != 0:
        print( "F ", end='')
    elif i % fizz != 0 and i % buzz == 0:
        print( "B ", end='')
    elif i % fizz == 0 and i % buzz == 0:
        print( "FB ", end='')
    else:
        print (i,"", end='')
        