x=[]
for i in range(3):
    r=[]
    for j in range(3):
        a=int(input(f'x[{i}][{j}]:'))
        r.append(a)
    x.append(r)
for d in x:
    print(d)
def check(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            if(i==j and x[i][j]!=1):
                print('not identity')
            elif(i!=j and x[i][j]!=0):
                print('not identity')
    else:        
        print('the given matrix is identity')
print(check(x))
            