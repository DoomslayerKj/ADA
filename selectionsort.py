#assignment_3

import time
import random

def selection_sort(A):
    start_time=time.time()
    length=len(A)
    for i in range(len(A)): 
      
 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
                A[i], A[min_idx] = A[min_idx], A[i] 
    end_time=time.time()
    print("Sorted array : ", A)
    print("Time Taken for " , length, " number of elements is :", end_time-start_time)



lis=[]
ch=int(input(" 1 for MANUAL , 2 for AUTO with RANGE input : "))
if ch==1:
    n=int(input("Enter the array size : "))
    print("Enter array : ")
    for i in range(0,n):
        ele=(int(input()))
        lis.append(ele)
elif ch==2:
    num=int(input("Enter number of elements : "))
    for i in range(0,num):
        lis.append(random.randrange(0,num))

print("\n The array is : ",lis)
for i in range(3):
    print("")
selection_sort(lis)



