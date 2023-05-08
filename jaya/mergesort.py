def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        sub_array1=arr[:mid]
        sub_array2=arr[mid:]
        mergesort(sub_array1)
        mergesort(sub_array2)
        i=j=k=0
        while i<len(sub_array1) and j<len(sub_array2):
            if sub_array1[i]<sub_array2[j]:
                arr[k]=sub_array1[i]
                i=i+1
            else:
                arr[k]=sub_array2[j]
                j=j+1
            k=k+1
        while i<len(sub_array1):
                arr[k]=sub_array1[i]
                i=i+1
                k=k+1
        while j <len(sub_array2):
                arr[k]=sub_array2[j]
                j=j+1
                k=k+1
#main
n=int(input("enter the total no.of elements to add in an array:"))
arr=[]
print("enter the elements:")
for i in range(0,n):
    s=int(input())
    arr.append(s)
print("before merge sort:")
for i in range(len(arr)):
    print(arr[i])
mergesort(arr)
print("after merge sort:")
for i in range(len(arr)):
    print(arr[i])
    
