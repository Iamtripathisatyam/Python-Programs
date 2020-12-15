a,b=[],[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

c=int(input("From Which: "))
b.append(a[:c])

d=[k for k in a if k not in b[0]]
d.extend(b[0])
print(d)
