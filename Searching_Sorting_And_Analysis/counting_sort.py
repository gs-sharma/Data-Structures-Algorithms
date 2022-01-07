def countSort(arr):
    #Length of array
    n = len(arr);
    max_value = max(arr)
    
    count = [0]*(max_value+1)
    result = [0]*(n)
    
    for i in range(n):
        count[arr[i]] +=1
        
    for i in range(1,max_value+1):
        count[i] += count[i-1]
        
    i = n-1
    while i >= 0:
        result[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    
    return result
    

if __name__ == "__main__":
    print("Enter the elements of array seprated by comma")
    input_arr = input()
    arr = input_arr.split(",")
    arr = list(map(int,arr))
    arr = countSort(arr)
    print(f"Sorted Array : \n {arr}")
    
    