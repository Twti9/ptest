def quickSort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if i<=pivot]
        great = [i for i in arr[1:] if i > pivot]
        return quickSort(less)+[pivot]+quickSort(great)
arr=[1,4,8,5,9,45,4,8,45]
print(quickSort(arr))
