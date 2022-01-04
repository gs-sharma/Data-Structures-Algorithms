"""
This program implemets Insertion Sort Algorithm
Input - Comma Seprated integer values that we want to sort 
Output - Sorted Array
"""
def insertion_sort(arr):
    #range is from 1 to len or array as 1st sub array is always sorted
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        while (i >=0 and arr[i]>key):
            arr[i+1] = arr[i]
            i -= 1
        #Inserting key to correctposition i.e., at the position of last element that is replaced
        # i+1  as we are performing i-1 in the while loop
        arr[i+1] = key
    
    return arr

if __name__ == "__main__":
    print("Enter the elements of array seprated by comma")
    input_arr = input()
    arr = input_arr.split(",")
    #Apply int method to all elements or the list 
    #Convert from map type to list type
    arr = list(map(int,arr))
    arr = insertion_sort(arr)
    print(f"Sorted Array : \n {arr}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    9
			
			
