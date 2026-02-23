arr = list(map(int, input("enter the number: ").split()))

if len(arr) < 2:
    print("there is no second element in array")
else:
    arr.sort()
    print("second largest", arr[-2])