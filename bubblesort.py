import time
def bubble_sort(a):
    n = len(a)
    start_time=time.time()
    for i in range(n):
        for j in range(0,n-i-1):
            if (a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    end_time=time.time()
    print("the sorted array is :",a)
    print("The time taken is : ",time.time()-start_time)

num=int(input("Enter array size : "))
list=[]
for i in range(0,num):
    ele=int(input("ENTER ARRAY : "))
    list.append(ele)
print(list)

bubble_sort(list)


#def selection_sort()




    