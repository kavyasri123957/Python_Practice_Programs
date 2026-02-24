a=[[1,2],[3,4]]
b=[[1,2],[3,4]]
result=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        result[i][j]=a[i][j]-b[i][j]
for k in result:
    print(k)