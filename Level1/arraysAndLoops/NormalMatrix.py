# Matrix is a rectangular arrangement of data or numbers. In other words, it is a rectangular array of data or numbers. 
# The horizontal entries in a matrix are called as ‘rows’ while the vertical entries are called as ‘columns’. 
# If a matrix has r number of rows and c number of columns then the order of matrix is given by r x c. 
# Each entries in a matrix can be integer values, or floating values, or even it can be complex numbers.


r=int(input())
c=int(input())
a=[]
for i in range(r):
    arr = []
    for j in range(c):
        arr.append(int(input()))
    a.append(arr)
for i in range(r):
    for j in range(c):
        if i == r-1 and j == c-1:
            print(a[i][j],end="")
        else:
            print(a[i][j],end=" ")
    print()