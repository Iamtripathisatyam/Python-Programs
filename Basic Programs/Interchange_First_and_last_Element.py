
################################## Approach #1:

def swap(a,size):
    a[0],a[size-1]=a[size-1],a[0]
    return a

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

swap(a,len(a))
print(a)

############################# Approach #2:

def swap(a):
    a[0],a[-1]=a[-1],a[0]
    return a

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

swap(a)
print(a)


######################### Approach #3:

def swap(a):
    start,*middle,end=a
    a=[end,*middle,start]
    return a

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

print(swap(a))



############################ Approach #4:

def swap(a):
   first=a.pop(0)
   last=a.pop(-1)
   a.insert(0,last)
   a.append(first)
   return a

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

print(swap(a))
