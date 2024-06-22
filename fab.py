#fibonacci series
num= int(input("enter number: "))
num0=0
num1=1
num2=0
for i in range(num):
    print(num2,end=" ")
    num0=num1
    num1=num2
    num2=num0+num1