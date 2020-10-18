class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        
        # If count is 3 or higher, multiply it by 0.9
        if count >= 3:
            total_price *= 0.9
        
        # Round total_price to the nearest whole number and return it
        return round(total_price)

menu_item1 = MenuItem('Sandwich', 5)
menu_item2 = MenuItem('Chocolate Cake', 4)
menu_item3 = MenuItem('Coffee', 3)
menu_item4 = MenuItem('Orange Juice', 2)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for menu_item in menu_items:
    print(str(index) + '. ' + menu_item.info())
    index += 1

print('--------------------')

order = int(input('Enter menu item number: '))
selected_menu = menu_items[order]
print('Selected item: ' + selected_menu.name)

# Receive input from the console and set the count variable to it
count = int(input('Enter quantity (10% off for 3 or more): '))

# Call the get_total_price method
result = selected_menu.get_total_price(count)

# Output 'Your total is $____'
print('Your total is $' + str(result))
