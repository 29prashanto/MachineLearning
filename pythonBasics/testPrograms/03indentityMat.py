# WAP for identity Matrix
#
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1


matsize = int(input("Enter the matrix size: "))

for i in range(0, matsize):
    for j in range(0, matsize):
        if(i==j):
            print("1", sep=' ', end=' ')
        else:
            print("0", sep=' ', end=' ')

    print()
