# Name of student : Niranjan Patil.
# Title :List out given integer numbers in ascending order(use bubble sort).
# Batch :f1.
# Roll no : 617.
# Date : 06/09/2016.
#-------------------------------------------------------------------------------
array=list()
m=raw_input("Enter how many elements in list")
m=int(m)
for i in range(0,m):
        m1=raw_input("Enter the elements :")
        m1=int(m1)
        array.append(m1)
print" Given list is :",array
for j in range(0,m-1):
     for k in range(0,m-1):
         if(array[k]>array[k+1]):
             temp=array[k]
             array[k]=array[k+1]
             array[k+1]=temp
print" Sorted list is : ",array