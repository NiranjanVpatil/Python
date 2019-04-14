# Name      : Niranjan patil.
# Title     : solve the fibonacci series in python.
# Batch     : f1.
# Roll no   : 617.
# Date      :25/08/2016.
#-------------------------------------------------------------------------------
a=raw_input("Enter how many terms :")
ai=int(a)
print ("fibonacci series upto"),ai
print"terms:"
b=0
print b
c=1
print c
n=1
while(n<=ai-2):
      d=b+c
      print d
      b=c
      c=d
      n=n+1


