def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1] , arr[j]
                
    return arr
    
    
if __name__ == "__main__":
    print("Enter the elements of array seprated by comma")
    input_arr = input()
    arr = input_arr.split(",")
    
    arr = list(map(int,arr))
    arr = bubbleSort(arr)
    print(f"Sorted Array : \n {arr}")   