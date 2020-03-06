def countRotations(arr, n):
    min1= arr[0] 
    for i in range(0, n): 	
	if(min1>arr[i]):
	    min1= arr[i] 
	    min_index = i 
	    return min_index; 
    arr = [15, 18, 2, 3, 6, 12] 
    n = len(arr) 
    print(countRotations(arr, n)) 


