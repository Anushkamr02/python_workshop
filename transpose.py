def mat(r,c):
    x=[]
    for i in range(r):
        row=[]
        for j in range(c):
            a=int(input(f"x[{i}][{j}]:"))
            row.append(a)
        x.append(row)
    return x
r=int(input('enter the range of row:'))
c=int(input('enter the range of column:'))
x=mat(r,c)
t=[]
for i in range(c):
    row=[]
    for j in range(r):
        row.append(x[j][i])
    t.append(row)
for row in t:
    print(row)
