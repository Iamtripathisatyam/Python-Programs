############################## N largest element from the list  ######################

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

b=int(input("N: "))
print(sorted(a)[-b:])
