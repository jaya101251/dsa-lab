def quick_sort(arr):
    if len(arr) <=1:
     return arr
    pivot=arr[0]
    left=[]
    right=[]
    for i in range(1,len(arr)):
        if arr[i]<pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left)+[pivot]+quick_sort(right)
my_list=[32,434,23,1,424,23]
sorted_list=quick_sort(my_list)
print(sorted_list)   
