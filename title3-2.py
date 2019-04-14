# Name : sumit
# Title : even or odd no
#
# Batch : f1.
#Roll no : 617.
# Date : 30/08/2016.
#------------------------------------------------------------------------------
a=raw_input("enter a")
n=int(a)
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print"non prime"
            break
    else:
            print"prime number"
else:
                print"non prime"






