
#-----------------------------------------JOIN FUNCTION---------------------------------------------------------


# list=["Satyam","Tripathi","Shivam","Tripathi","Deep","Tripathi","Shashank","Tripathi"]
# a=" & ".join(list)
# print(a)


#-----------------------------------------MAP FUNCTION---------------------------------------------------------


# l=["1","2","3","4","5"]
# for i in range(len(l)):
#     l[i]=int(l[i])
#     l[i]=l[i]+5
#     print(l[i])

# def sq(a):
#     return a*a
# num=[1,2,3,4,5,6,7,8,9]
# b=list(map(sq,num))
# print(b)


# num=[1,2,3,4,5,6,7,8,9]
# b=list(map(lambda x:x*x , num))
# print(b)


# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func=[square,cube]
#
# for i in range(10):
#  c=list(map(lambda x:x(i),func))
#  print(c)



#-----------------------------------------FILTER FUNCTION---------------------------------------------------------


# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# b=list(filter(lambda x : x>5 , a))
# print(b)



#-----------------------------------------REDUCE FUNCTION---------------------------------------------------------



# from functools import reduce
# a=[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]
# b=reduce(lambda x ,y : x+y , a)
# print(b)

