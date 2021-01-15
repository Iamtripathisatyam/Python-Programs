a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

j=0
for i in range(0,n):
    if a[i]<0:
        a[i],a[j]=a[j],a[i]
        j+=1
print(f"Array with negative elements at one side: {a}")
