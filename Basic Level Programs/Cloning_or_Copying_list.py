################################## Cloning or Copying a List ########################

############### 1st Approach

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

b=a[:]
print(*b)



############### 2nd Approach

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

b=[]
b.extend(a)
print(*b)



############# 3rd Approach

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

b=list(a)
print(*b)



################# 4th Approach

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

b=[i for i in a]
print(*b)


################# 5th Approach

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

b=a.copy()
print(*b)
