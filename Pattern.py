"""a=int(input("Enter number of rows :"))
b=int(input("Enter number of columns:"))
for i in range(0,a):
    for j in range(0,b):
        print("*",end="")
    print()"""
n=int(input())
for i in range(1,n+1):
    for j in range(n+1):
        print(i,end='')
        
    #print("1",end='')
    print("\n")
