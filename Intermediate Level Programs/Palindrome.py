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
    for i in range(n):
        print(f"Next palindrome of {numbers[i]} is : {next_palindrome(numbers[i])}")

