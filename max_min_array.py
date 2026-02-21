arr=[12,34,78,98]
max_val=arr[0]
min_val=arr[0]
for i in range(len(arr)):
    if arr[i]>max_val:
        max_val=arr[i]
    if arr[i]<min_val:
        min_val=arr[i]

print("max value",max_val)
print("min value",min_val)