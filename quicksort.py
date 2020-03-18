import time


def partition(arr,low,high): 
    i = ( low-1 )        
    pivot = arr[high]     
  
    for j in range(low , high): 
  
       
        if   arr[j] < pivot: 
          
           
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  


def quickSort(arr,low,high):
  
    if low < high: 
  
       
        pi = partition(arr,low,high) 
  
        
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  

arr=[]
print("Enter array after the next enter : ")
for i in range(int(input("Enter array size : "))):
    ele=int(input("Element : "))
    arr.append(ele)
start=time.time()
n = len(arr) 
quickSort(arr,0,n-1)
end=time.time()
print("The time taken is : ",end-start)
print ("Sorted array is:") 
for i in range(n): 
    print ( arr[i])

  