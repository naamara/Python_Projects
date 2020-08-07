""" A simple Restaurant Menu calculator

This project is for helping Hannington and his employees generate total amount of items ordered by
clients in his Restaurant.

This project also helps to serve or give out the correct items ordered by clients within a short period of time.

It is written by Hannington Naamara - Scholar Network Python Bootcamp student as a capstone project.

"""

print(__doc__)

# create a menu dictionary for items as keys and price as values
menu = {'Chicken': 3.50, 'Pork': 2.50, 'Pizza': 4.00,
        'Hot dog': 3.50, 'Egg': 1.75, 'Milk Shake': 2.25,
        'Salad': 3.75, 'Cock Tail': 1.25,
        'Potato Crisps': 4.57
        }

# create a list to call the dictionary values from the menu dictionary
menuitems = ['Chicken', 'Pork', 'Pizza', 'Hot dog', 'Egg', 'Milk Shake',
             'Salad', 'Cock Tail', 'Potato Crisps'
             ]


def print_menu(menu_list, menu_dic):
    """
    :param menu_list: print put the item name for Hannington's Restaurant
    :param menu_dic: prints the price which is the value corresponding to the key in a menu dictionary.
    :return: the menu showing the item number, name and its price.

    """
    print()
    print("Hannington's Restaurant Menu")
    print()
    orderNum = 1
    for i in menu_list:
        print(str(orderNum) + '. ' + i + ' - ' + '$' + str(menu_dic[i]))
        orderNum += 1


print_menu(menuitems, menu)

while True:
    # This functions ensures the client inputs a valid client input by
    # requesting integer input before converting to a string
    while True:
        try:
            order = int(input('\nEnter your order (1-9) or (press 0 to quit): '))
        except ValueError:
            print("Please enter numbers (1-9) only.")
        else:
            break

    if order == 0:
        print("\n" + "Thank you for placing your order with Hannington's Restaurant!")
        break

   
    def print_order(client_order):
        """
        :param client_order:  for displaying the menu order of the client.
        :return: the clients order and the number of times an item is ordered (Quantity).
        """
        print()
        print("Client's Order")
        print("Quantity", end="\t\t")
        print("Item", end="\n")
        for i in range(1, 10):
            if client_order.count(str(i)) > 0:
                print(str((client_order.count(str(i)))), end="\t\t\t")
                print(str(menuitems[i - 1]))


    # convert client's int input into a string
    order = str(order)

    # Print client's order
    print_order(order)

    # calculate a total sum of money to be paid by the client.
    total = 0
    for num in order:
        total += float(menu[menuitems[int(num)-1]])

    print('\nThe total amount to be paid by a client is: $', total)

