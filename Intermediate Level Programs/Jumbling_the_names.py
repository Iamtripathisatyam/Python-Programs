import random
import time
def jumble_word(first_name, last_name, num):
    print("\n\nNames after Jumbling : ")
    for i in range(0, num):
        jumbled_name= first_name[i].capitalize() +" " +last_name[random.randint(0, num - 1)].capitalize()
        time.sleep(0.5)
        print(jumbled_name)

if __name__ == '__main__':
    num = int(input("How many names you want to input : "))
    nameList = []
    first_name = []
    last_name = []
    for i in range(1, num + 1):
        name = input(f"Enter {i} name:")
        # name=name.upper()
        if name.isnumeric():
            raise Exception("Here Numbers are not Allowed !!")
        nameList.append(name)
    for i in nameList:
        split_name = i.split(" ")
        first_name.append(split_name[0])
        last_name.append(split_name[1])

    jumble_word(first_name, last_name, num)


