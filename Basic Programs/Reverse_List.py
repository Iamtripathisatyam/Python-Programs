def reverse(a,i,j):
     while i<=j:
         a[i],a[j]=a[j],a[i]
         i+=1
         j-=1

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

reverse(a,0,len(a)-1)
print(a)
