num1=int(input("enter the number"))
num2=int(input("enter the number"))
a,b=num1,num2
while b!=0:
    a,b=b,a%b
gcd=a
lcm=(num1*num2)//gcd
print(gcd)
print(lcm)
