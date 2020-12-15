def sorter(a,end):
    start=mid=0
    pilot=1
    while mid<=end:
        if a[mid]<pilot:
            a[mid],a[start]=a[start],a[mid]
            mid+=1
            start+=1
        elif a[mid]>pilot:
            a[mid],a[end]=a[end],a[mid]
            end-=1
        else:
            mid+=1

a,b=[],[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

sorter(a,len(a)-1)
print(a)
