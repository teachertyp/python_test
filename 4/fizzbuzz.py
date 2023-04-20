import sys
#filename = sys.argv[1]
# далі відкриваємо файл для читання (опція 'r')

def fizzbuzz(fizz,buzz,c):
    s =""
    for i in range(1,c+1):
        if i == 1:
            s += " "+str(i)
        elif i % fizz == 0 and i % buzz != 0:
            s += "F "
        elif i % fizz != 0 and i % buzz == 0:
            s += "B "
        elif i % fizz == 0 and i % buzz == 0:
            s += "FB "
        else:
            s+=str(i)+" "
    s+="\n"
    return s

finput = open('/home/typ/GIT/python/git/tested/4/fizzbuzz.in', 'r')
foutput = open('/home/typ/GIT/python/git/tested/4/fizzbuzz.out', 'w')
for line in finput:
    line_values = line.split()
    a = int(line_values[0])
    b = int(line_values[1])
    c = int(line_values[2])
    foutput.write(fizzbuzz(a,b,c))
finput.close()
foutput.close()