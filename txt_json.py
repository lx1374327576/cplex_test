g = open('test.txt')

f = open('out.txt', 'w')
line = g.readline()
while line:
    line = line.replace('\n', '')
    p = line.split(',')
    print('\"%s\":\"%s\",' % (p[0], p[1]), file=f)
    line = g.readline()
g.close()
f.close()

