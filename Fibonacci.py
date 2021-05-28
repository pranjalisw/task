#Python Program for Fibonacci numbers.
max = int(input("Enter the number upto which you want a fibonacci series " ))
num1=0
num2=1
count=0
if (max <= 0):
    print("Enter positive number")
elif (max == 1):
    print("fibonacci series upto " ,max, ":")
    print(num1,max)
else:
    print("fibonacci series:" , end = "  " )
    while count <= max :
        print(num1, end = " " )
        num3= num1 + num2
        num1 = num2
        num2 = num3
        count= count+1
