a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=input()
    a.append(element)

k=int(input("Add: "))
result=[]
for ele in a:
    if ele.isdigit():
        result.append(str(int(ele)+k))
    else:
        result.append(ele)

print(result)
