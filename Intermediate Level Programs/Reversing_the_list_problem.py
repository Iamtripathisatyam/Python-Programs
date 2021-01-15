size=int(input("Enter size of list : "))
mylist=[]
for i in range(size):
    mylist.append(int(input(f"Enter {i+1} element : ")))
print(f"Your list is : {mylist}\n")

reverse1 = mylist[:] # Copying the list to the reverse1 variable...
reverse1.reverse()   # 1st method of reversing the list...

reverse2 = mylist[::-1]

reverse3 = mylist[:]
for i in range(len(reverse3) // 2):
    reverse3[i], reverse3[len(reverse3) - i - 1] = reverse3[len(reverse3) - i - 1], reverse3[i]

print(f"My First reversed list of {mylist} is : {reverse1}")
print(f"My Second reversed list of {mylist} is : {reverse2}")
print(f"My Third reversed list of {mylist} is : {reverse3}")

if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods give same result\n")


