rows=int(input("enter no. of rows:"))
columns=int(input("enter no. of columns:"))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(columns):
        a=int(input())
        row.append(a)
    matrix.append(row)
for row in matrix:
    print(row)
diagonal_sum = 0
if rows==columns:
    for i in range(rows):
        diagonal_sum += matrix[i][i]
    print("Sum of diagonal elements:", diagonal_sum)
else:
    print("Matrix is not square matrix")
 