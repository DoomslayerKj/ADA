import time

def insert(a):
    start=time.time()
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
             a[j+1] = a[j]
             j -= 1
        a[j+1] = key 
        end=time.time()
    print("Sorted Array : ")
    
    for i in range(0,len(a)):
        print(a[i])
    print("Time Taken for ",len(a)," Elements is : ",end-start,"s")

lis=[]
n=input("Size of array : ")
print("enter Array : ")
for i in range(0,n):
    ele=int(input())
    lis.append(ele)

insert(lis)
