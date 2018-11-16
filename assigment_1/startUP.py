import sys

def nonZero_1(arr):

    count = 0
    boolean = True

    for i in reversed(arr):
#         print(count)
        #     print(sum(i))

        if sum(i) != 0 and count == 0:
            count = count + 1
            boolean = True
        elif sum(i) == 0 and count == 0:
#             print('yes')
            boolean = True
        elif sum(i) == 0 and count > 0:
            return False
    return boolean


def allExceptPivot_4(arr, arrFoo,row,col):

    a = True

    for i in range(row):
        for j in range(col):
            if arr[i][j] > 0 and ((i, j)not in arrFoo):
                return False
            else:
                a = True
    return a


def pivot_1_3(arrFoo, arr):
    a = True
    for k, v in arrFoo:
        if arr[k][v] == 1:
            a = True
        else:
            a = False
            break
    return a


def occurance_2(arr,row,col):

    a=True
    b=False
    arrFoo = []
    arrTemp = []

    for i in range(row):
        for j in range(col):
            if arr[i][j]>0:
                arrTemp.append(j)
                arrFoo.append((i,j))
                break
#     print(arrTemp)
    for i in arrTemp:
        if arrTemp.count(i)>1:
            a = False
            break
        else:
            a = True

#     print(arrFoo)
    if arrTemp != sorted(arrTemp):
        return False

    return a and allExceptPivot_4(arr,arrFoo,row,col) and pivot_1_3(arrFoo, arr) and nonZero_1(arr)


def is_reducedEchelon_form(matrix, row, col):
	# your code here
	return occurance_2(matrix, row, col)

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



    if(is_reducedEchelon_form(matrix,row,col)):
        output.write('True\n')
    else:
        output.write('False\n')
in_.close()
output.close()
