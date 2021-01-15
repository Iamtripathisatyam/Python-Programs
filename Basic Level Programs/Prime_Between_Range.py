def prime(a,b):
    for i in range(a,b):
        if i>1:
            for j in range(2,i//2):
                 if(i%j==0):
                     break
            else:
                print(i)
a=int(input("Enter Lower Range: "))
b=int(input("Enter Upper Range: "))
prime(a,b)
