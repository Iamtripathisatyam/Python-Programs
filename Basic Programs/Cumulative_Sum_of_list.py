####################################### find Cumulative sum of a list #########################

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

new=[]
j=0
for i in range(len(a)):
    j+=a[i]
    new.append(j)

print(new)
