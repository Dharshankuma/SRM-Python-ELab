# Matrix is a rectangular arrangement of data or numbers. In other words, it is a rectangular array of data or numbers. 
# The horizontal entries in a matrix are called as ‘rows’ while the vertical entries are called as ‘columns’. 
# If a matrix has r number of rows and c number of columns then the order of matrix is given by r x c. 
# Each entries in a matrix can be integer values, or floating values, or even it can be complex numbers.

#Concept used -> Trasnpose of Matrix
# Transpose means: Rows become columns and Columns become rows

r = int(input())
c = int(input())
a = []
for i in range(r):
    row = []
    for j in range(c): row.append(int(input()))
    a.append(row)
for j in range(c):
    for i in range(r):
        if j == c-1 and i == r-1:
            print(a[i][j], end="")
        else:
            print(a[i][j], end=" ")
            
    print()