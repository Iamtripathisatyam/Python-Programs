
#-------------------------GENERATORS------------------------------------#
# iterable-  __iter__() or __getitem__()
# iterator-  __next__()
# iteration
# def gen(n):
#     for i in range(n):
#          yield i
        #  return i




#-------------------Factorial----------------------

# def Factorial_gen(n):
#     fac = 1
#     for i in range(n):
#         fac = fac*(i+1)
#         yield fac
#         # return fac
# number = int(input("Enter a number : "))
# print(Factorial_gen(number))
#-----------------------Fibonacci----------------------------------
# def fibonacci_gen(n):
#     if n == 1:
#         yield 0
#     elif n == 2:
#         yield 1
#     else:
#         yield fibonacci_gen(n-1) + fibonacci_gen(n-2)
# num = int(input("Enter the number:"))
# print(fibonacci_gen(num))
# # g=gen(3)
# # print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# g="SATYAM EMPIRE"
# for c in g:
#     print(c)
# print(iter(g))
# sat=iter(g)
# print(sat.__next__())
# print(sat.__next__())
# print(sat.__next__())

#-----------------------Python Comprehensions-------------------------------
# sat=[]
# for i in range(100):
#     if i%3 ==0:
#         sat.append(i)
#
# print(sat)

# sat=[i for i in range(100)]
# print(sat)
# sat=[i for i in range(1,101)]
# print(sat)
# sat=[i for i in range(100) if i%2==0]
# print(sat)

# dict1={i:f"Item{i}" for i in range(100)}
# print(dict1)
# dict1={i:f"Item{i}" for i in range(10000) if i%100==0}
# print(dict1)

# dict1={i:f"Item{i}" for i in range(10)}
# dict2={value:key for key,value in dict1.items()}
# print(dict1,"\n",dict2)
#
# satyam={tri for tri in ["Mahoba","Banda","Mahoba","Banda","Mahoba","Banda"]}
# print(satyam)
# print(type(satyam))
# satyam=[tri for tri in ["Mahoba","Banda","Mahoba","Banda","Mahoba","Banda"]]
# print(satyam)
# print(type(satyam))

# evens=(i for i in range(2,22) if i%2==0)
# print(type(evens))
# print(evens)
# for i in evens:
#     print(i)
