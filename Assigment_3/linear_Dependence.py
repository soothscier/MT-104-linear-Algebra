import numpy

def nonZero(a):
    b=[]
    pcount = 0

    for i in range(len(a)):
        pcount = 0
        for j in range(len(a[i])):
            if a[i][j]==0:
                pcount = pcount +1
                if pcount == len(a[i]):
                    b.append((pcount, a[i]))
            else:
                b.append((pcount, a[i]))
                break

    b = sorted(b)
    c = []

    for i in range(len(b)):
        c.append(b[i][1])
    return c


def reduced(a):
    a = nonZero(a)
    temp = 0

    for i in range(len(a)):

        for j in range(len(a[i])):

            if not(a[i][j] == 0):
                a[i] = [x / a[i][j] for x in a[i]]
                a = rowElimination(a, a[i], j)

                break

    for i in range(len(a)):
        for j in range(len(a[i])):
            if (a[i][j] == -0.0 or a[i][j]==0.0 or a[i][j] == 1.0 or a[i][j] == -1.0):
                a[i][j] = a[i][j] * a[i][j]
                a[i][j] = int(a[i][j])


    return a


def rowElimination(a, indexArr, ind): #ind = j

    tempArr = numpy.array(indexArr)
    tempArr2 = 0

    for i in range(len(a)):
        if a[i] == indexArr:
            continue

        else:
            for j in range(len(a)):
                tempArr = numpy.array(indexArr)

                if a[j] == indexArr:
                    continue

                tempArr = tempArr * a[i][ind]
                for k in range(len(a[i])):
                    a[i][k] = tempArr[k] - a[i][k]

    return a

def linearDependance(a, row, col):
    if len(a[0]) > len(a):
        return False
    else:
        a = reduced(a)
        for i in range(len(a)):
            if sum(a[i]) != 1:
                return False
        return True

matrix = []
in_ = open('in.txt','r')
output=open('out.txt','a')
tmatrix = int(in_.readline())
for m in range(tmatrix):
    del matrix[:]
    row = int(in_.readline())
    col = int(in_.readline())
    for r in range(row):
        matrix.append(list(map(int,in_.readline().strip().split())))
    #print(matrix)



    if(linearDependance(matrix,row,col)):
        output.write('True\n')
    else:
        output.write('False\n')
in_.close()
output.close()
