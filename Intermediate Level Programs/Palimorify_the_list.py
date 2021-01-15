def next_palindrome(n):
    n = n+1
    while True:
     if str(n)==str(n)[::-1]:
        return n
     else:
        n+=1
if __name__ == "__main__":
    n = int(input("Enter the number of test cases : "))
    numbers = []
    for i in range(n):
        number = int(input(f"Enter {i+1} number : \n"))
        numbers.append(number)
    print(f"Your List : {numbers}")
    print(f"O/p List  : {[numbers[i] if numbers[i]<10 else next_palindrome(numbers[i]) for i in range(n)]}")

