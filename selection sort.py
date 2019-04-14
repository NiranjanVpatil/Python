# Name:
#-------------------------------------------------------------------------------
array=list()
m=raw_input("Enter how many elements in list")
m=int(m)
for i in range(0,m):
        m1=raw_input("Enter the elements :")
        m1=int(m1)
        array.append(m1)
print" Given list is :",array
min=int()
for i in range(0,m-1):
    min=i
    for j in range(i+1,m):
        if(array[j]<array[min]):
            min=j
    if(min != i):
            temp=array[i]
            array[i]=array[min]
            array[min]=temp
print" Sorted list is : ",array