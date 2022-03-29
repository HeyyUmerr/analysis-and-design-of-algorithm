array = [89,64,23,10,67,78]
def Linear_search(array,element):
    for i in array:
        if (i == element):
         return True
        else:
            return False
         
      
element = int(input())
result = Linear_search(array,element)
if (result == True):
    print("Element is present")
else:
    print("element not found")
