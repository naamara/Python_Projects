# This is a simple inventory program for a small car dealership.

#Password to access the delete and edit feature is 'admin'

print('VEHICLE INVENTORY SYSTEM')


class Automobile:
    def __init__(self):
        self._make = ''
        self._model = ''
        self._year = 0
        self._color = ''
        self._mileage = 0
        self._cost = 0



    def addVehicle(self):
        while True:
            try:

                userin = self._make = (input('Enter vehicle make: ').title())
                while not userin.isalpha():
                    print('Please enter only alphabets for vehicle make')
                    userin = self._make = (input('Enter vehicle make: ').title())



                self._model = input('Enter vehicle model: ').title()

                useryear = self._year = (input('Enter vehicle year: '))
                while not useryear.isnumeric():
                    print('Only numbers is required for vehicle year ')
                    useryear = self._year = (input('Enter vehicle year: '))


                usercolor = self._color = input('Enter vehicle color: ').title()
                while not usercolor.isalpha():
                    print('Please enter only alphabets for vehicle color')
                    usercolor = self._color = input('Enter vehicle color: ').title()
                usermile = self._mileage = (input('Enter vehicle mileage: '))
                while not usermile.isnumeric():
                    print('Please input only numbers for vehicle mileage')
                    usermile = self._mileage = (input('Enter vehicle mileage: '))

                usercost = self._cost = (input('Enter the vehicle cost: '))
                while not usercost.isnumeric():
                    print('Input only numbers for vehicle cost')
                    usercost = self._cost = (input('Enter the vehicle cost: '))

                return True
            except ValueError:
                print('Please try entering vehicle information again using only whole numbers, with no commas or symbols, for mileage, cost and year')
                continue

    def __str__(self):
        return '\t'.join(str(x) for x in [self._make, self._model, self._year, self._color, self._mileage, self._cost])


class Inventory:
    def __init__(self):
        self.vehicles = []

    def addVehicle(self):
        vehicle = Automobile()
        if vehicle.addVehicle() == True:
            self.vehicles.append(vehicle)
            print()
            print('This vehicle has been added, Thank you')



    def viewInventory(self):
        print('\t'.join(['', 'Make', 'Model', 'Year', 'Color', 'Mileage', 'Cost']).title())
        for idx, vehicle in enumerate(self.vehicles):
            print(idx + 1, end='\t')
            print(vehicle)


inventory = Inventory()
while True:

    print('#1 Add Vehicle to Inventory')
    print('#2 Delete Vehicle from Inventory')
    print('#3 View Current Inventory')
    print('#4 Edit vehicle in Inventory')
    print('#5 Export Current Inventory')
    print('#6 Quit')
    userInput = input('Please choose from one of the above options: ')
    if userInput == "1":
        print(
            'Please try entering vehicle information using only whole numbers with no comma or symbols for mileage, cost and year')
        # add a vehicle
        inventory.addVehicle()

    elif userInput == '2':
        # delete a vehicle
        while True:
                password = (input('Please enter the password to delete a vehicle: '))
                if password == 'admin':
                    if len(inventory.vehicles) < 1:
                        print('Sorry there are no vehicles currently in inventory')
                        break


                    try:
                        inventory.viewInventory()
                        item = int(input('Please enter the number associated with the vehicle to be removed: '))
                        if item  > len(inventory.vehicles):
                            print('This is an invalid number')
                            continue
                        else:
                            inventory.vehicles.remove(inventory.vehicles[item - 1])
                            print()
                            print('This vehicle has been removed')
                            break
                    except ValueError:
                            print('Please type in only the number associated to the vehicle you want to delete')
                            continue

                else:
                    print('INCORRECT PASSWORD!!! Please contact the admin to get the password')
                    continue
        continue


    elif userInput == '3':
        # list all the vehicles
            if len(inventory.vehicles) < 1:
                print('Sorry there are no vehicles currently in inventory')
                continue
            inventory.viewInventory()
    elif userInput == '4':
        # edit vehicle
        while True:
                password = (input('Please enter the password to edit a vehicle: '))
                if password == 'admin':
                    if len(inventory.vehicles) < 1:
                        print('Sorry there are no vehicles currently in inventory')
                        break

                    try:
                        inventory.viewInventory()
                        item = int(input('Please enter the number associated with the vehicle to be updated: '))
                        if item > len(inventory.vehicles):
                            print('This is an invalid number')
                            continue
                        else:
                            automobile = Automobile()
                            if automobile.addVehicle() == True:
                                inventory.vehicles.remove(inventory.vehicles[item - 1])
                                inventory.vehicles.insert(item - 1, automobile)
                                print('This vehicle has been edited')
                                break
                    except ValueError:
                                print('Please input only the number that is associated to the vehicle you want to edit ')
                                continue
                else:
                    print('INVALID PASSWORD!!! Contact the admin')
                    continue
        continue
    elif userInput == '5':
        # export inventory to file
        if len(inventory.vehicles) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        f = open('vehicle_inventory.txt', 'w')
        f.write('\t'.join(['Make', 'Model', 'Year', 'Color', 'Mileage', 'Prize']))
        f.write('\n')
        for vechicle in inventory.vehicles:
            f.write('%s\n' % vechicle)
        f.close()
        print('The vehicle inventory has been exported to a file')
    elif userInput == '6':
        # exit the loop
        print('Goodbye')
        break
    else:
        # invalid user input
        print('This is an invalid input. Please try again.')