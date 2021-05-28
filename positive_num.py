#Python program to print all positive numbers in a range.
list1= [12, 13, -35, 17, -9]
i=0
length=len(list1)
while( i < length):
        if(list1[i] > 0):
           print(list1[i] , end = " " )
        i = i+1
print("\n")

list2= [12, 14, -95, 3]
j=0
length2=len(list2)
while( j < length2):
    if(list2[j]>0 ):
       print(list2[j] , end = " " )
    j = j + 1
