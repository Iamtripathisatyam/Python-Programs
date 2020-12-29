##################################  Count occurrences of an element in a list #############

####################### 1st Approach

def occur(a,b):
    count=0
    for ele in a:
       if ele==b:
           count+=1
    return count

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

b=int(input("Enter the Element you want to search for: "))
print(f"{b} Occured {occur(a,b)} times...")


#################### 2nd Approach

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)
b=int(input("Enter the Element you want to search for: "))
print(f"{b} Occured {a.count(b)} times...")
