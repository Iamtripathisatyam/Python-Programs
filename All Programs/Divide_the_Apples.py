apples = int(input("Enter the number of apples : "))
mn = int(input("Enter the minimum number : "))
mx = int(input("Enter the maximum number : "))

for i in range(mn, mx+1):
    if apples%i == 0:
        print(f"{i} is a divisor of {apples}")
    else:
        print(f"{i} is not a divisor of {apples}")
