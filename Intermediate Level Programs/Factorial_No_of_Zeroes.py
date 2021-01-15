def fac(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fac(num-1)
def fact(num):
    i=5
    count=0
    if num//i!=0:
        count+=int(num//i)
        # count += int(num / i)
        i=i*5
    return count

if __name__ == '__main__':
    a=int(input(" Please Enter a no. : "))
    print(f" Factorial is : {fac(a)}")
    print(f" No. of Zeroes in the factorial : {fact(a)}")
