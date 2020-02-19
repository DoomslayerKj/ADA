import time
lis=[]

def search_large(A,k):
    start=time.time()
    length=len(A)
    for i in range(len(A)): 
      
 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
    A.sort(reverse = True)
    for j in range(0,k):
            print(A[j])
    end=time.time()
    #print("Largest : ",max)
    print("time taken for ",len(A)," elements is :",end-start)



n=int(input("Enter the array size : "))
print("Enter array : ")
for i in range(0,n):
    ele=(int(input()))
    lis.append(ele)

k=int(input("Enter the value of  K : "))
search_large(lis,k)
