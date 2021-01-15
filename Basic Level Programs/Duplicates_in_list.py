#################################### print duplicates from a list ####################

def repeat(a):
    size=len(a)
    repeated=[]
    for i in range(size):
        k=i+1
        for j in range(k,size):
            if a[i]==a[j] and a[i] not in repeated:
                repeated.append(a[i])
    return repeated

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

print(*repeat(a))
