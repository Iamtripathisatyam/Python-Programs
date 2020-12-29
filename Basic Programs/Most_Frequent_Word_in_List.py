from collections import defaultdict

a = []
n = int(input("Enter the Number of Elements: "))
for i in range(0, n):
    element = input()
    a.append(element)

temp = defaultdict(int)
for ele in a:
    for elem in ele.split():
        temp[elem] += 1

print(temp)
result = max(temp, key=temp.get)
print(result)
