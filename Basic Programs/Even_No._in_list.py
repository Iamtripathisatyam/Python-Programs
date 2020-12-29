###################################### Even Number in list #######################

################### 1st Approach

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

b=[i for i in a if i%2==0]
print(*b)


############################# 2nd Approach

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

even=list(filter(lambda a: a%2==0,a))
print(*even)
