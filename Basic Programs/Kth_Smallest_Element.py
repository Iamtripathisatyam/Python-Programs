a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

k=int(input("Enter the K'th Element: "))
a.sort()
print(f"{k}'th Smallest: {a[k-1]}")
