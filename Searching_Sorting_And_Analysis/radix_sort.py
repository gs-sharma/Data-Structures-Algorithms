def countSort(arr,place):
    n = len(arr)
    result = [0]*n
    count = [0]*10
    
    #Calculcate count of each element 
    for i in range(n):
        index = arr[i]//place
        count[index%10] += 1
    
    #Cumulative Sum
    for i in range(1,10):
        count[i] += count[i-1]
        
    #Place at appropriate position in result
    i = n-1
    while i >= 0 :
        index = arr[i] // place
        result[count[index%10] - 1] = arr[i]
        count[index%10 ] -= 1
        i -=1
    return result
    
def radixSort(arr):
    max_element = max(arr)
    place = 1
    while max_element // place > 0:
        arr = countSort(arr,place)
        place *= 10
    return arr
        
if __name__ == "__main__":
    print("Enter the elements of array seprated by comma")
    input_arr = input()
    arr = input_arr.split(",")
    arr = list(map(int,arr))
    arr = radixSort(arr)
    print(f"Sorted Array : \n {arr}")