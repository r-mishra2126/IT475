a = [1, 2, 3] 
try:  
    print ("Second element = %d" %(a[1])) 
  
    # Throws error since there are only 3 elements in array 
    print ("Fourth element = %d" %(a[3]))  
  
except IndexError: 
    print ("An error occurred")
