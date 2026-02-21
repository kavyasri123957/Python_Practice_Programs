num=int(input("enter the number"))
temp=num
digits=len(str(num))
arm_sum=0
while temp>0:
    digit=temp%10
    arm_sum+=digit**digits
    temp=temp//10
if arm_sum==num:
    print("armstrong ")
else:
    print("not a arm strong")