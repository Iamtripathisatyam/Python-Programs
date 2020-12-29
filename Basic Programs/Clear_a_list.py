########################################## Ways to Clear a list #####################################

################### 1st Way:

a=[4,5,1,2,6,8,9,6]
print(f"Before Clear: {a}")
a.clear()
print(f"After Clear: {a}")


################# 2nd Way:

a=[4,5,1,2,6,8,9,6]
print(f"Before Clear: {a}")
a=[]
print(f"After Clear: {a}")


################ 3rd Way:

a=[4,5,1,2,6,8,9,6]
print(f"Before Clear: {a}")
a*=0
print(f"After Clear: {a}")


################# 4th Way:

a=[4,5,1,2,6,8,9,6]
print(f"Before Clear: {a}")
del a[:]
print(f"After Clear: {a}")
