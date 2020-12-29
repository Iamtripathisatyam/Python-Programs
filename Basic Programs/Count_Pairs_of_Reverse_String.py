a = []
n = int(input("Enter the Number of Elements: "))
for i in range(0, n):
    element = input()
    a.append(element)
count = 0
for ele in range(0, len(a)):
    for elem in range(ele, len(a)):
        if a[ele] == str("".join(list(reversed(a[elem])))):
            count += 1

print(count)
