array = [89,64,23,10,67,78]
def Linear_search(array,n,element):
    for i in range(0,n):
        if (array[i] == element):
         return True
    return False     
    
n=len(array)         
      
element = int(input())
result = Linear_search(array,n,element)
if (result == True):
    print("Element is present")
else:
    print("element not found")
