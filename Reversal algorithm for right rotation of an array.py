 def reverseArray( arr, start, end): 
	
	while (start < end): 
		
		arr[start], arr[end] = arr[end], arr[start] 
		start = start + 1
		end = end - 1
def rightRotate( arr, d, n): 
	
	reverseArray(arr, 0, n - 1); 
	reverseArray(arr, 0, d - 1); 
	reverseArray(arr, d, n - 1); 
def prArray( arr, size): 
	for i in range(0, size): 
		print (arr[i], end = ' ') 



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
n = len(arr) 
k = 3
	
 
rightRotate(arr, k, n) 
prArray(arr, n) 



