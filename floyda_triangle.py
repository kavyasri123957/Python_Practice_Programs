num=int(input("enter the input"))
n=1
for i in range(1,num+1):
    for j in range(i):
        print(n,end="")
        n+=1
    print()
        