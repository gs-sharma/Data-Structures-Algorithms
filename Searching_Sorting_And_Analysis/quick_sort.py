def partition(arr,start,stop):
    pivot = arr[start]
    i = start
    for j in range(start+1,stop+1):
        if arr[j] < pivot :
            i += 1
            arr[j] , arr[i] = arr[i] , arr[j]
    
    arr[start] , arr[i] = arr[i] , arr[start]
    return i
            

def quickSort(arr,start,stop):
    if stop > start:
        pivotIndex = partition(arr,start,stop)
        quickSort(arr,start,pivotIndex-1)
        quickSort(arr,pivotIndex+1,stop)
    return arr

if __name__ == "__main__":
    print("Enter the elements of array seprated by comma")
    input_arr = input()
    arr = input_arr.split(",")
    
    arr = list(map(int,arr))
    arr = quickSort(arr,0,len(arr)-1)
    print(f"Sorted Array : \n {arr}")   