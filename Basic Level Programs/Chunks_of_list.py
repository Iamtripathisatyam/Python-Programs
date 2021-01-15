##################################### Break a list into chunks of size N ####################

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)
m=int(input("Chunks: "))

b=[a[i:i+m] for i in range(0,len(a),m)]
print(b)
