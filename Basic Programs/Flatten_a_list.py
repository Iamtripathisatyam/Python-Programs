##################### Flatten a list #####################

################## 1st Approach

a=[[1,2,3],[4,5,6],[7,8,9,10]]
b=[]
for ele in a:
    if type(ele) is list:
        for j in ele:
            b.append(j)
    else:
        b.append(ele)
print(*b)

#################### 2nd Approach

def flatten(a):
    for ele in a:
        if isinstance(ele,list):
            yield from flatten(ele)
        else:
            yield ele


a=[[1,2,3],[4,5,6],[7,8,9,10]]
b=list(flatten(a))
print(b)
