######################################### Remove Multiple Elements from a list ###########################


################### 1st Approach

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

del a[1:3]
print(a)


################# 2nd Approach

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

b=[]
m=int(input("No. of Elements You want to Delete: "))
for i in range(0,m):
    element=int(input())
    b.append(element)

ele=[i for i in a if i not in b]
print(*ele)
