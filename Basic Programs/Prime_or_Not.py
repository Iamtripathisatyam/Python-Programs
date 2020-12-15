def prime(a):
    if a>1:
        for i in range(2,a//2):
            if(a%i==0):
                print("It's not a Prime Number")
                break
            else:
                print("It's a Prime Number")

a=int(input("Enter a Number: "))
prime(a)
