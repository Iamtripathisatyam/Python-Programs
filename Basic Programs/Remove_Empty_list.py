##################################### Remove Empty List ########################

############## 1st Approach

a=[1,2,[],3,[],5]
ele=list(filter(None,a))
print(ele)


############## 2nd Approach

a=[1,2,[],3,[],5]
ele=[i for i in a if i!=[]]
print(*ele)
