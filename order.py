import time
import datetime
from burger import *


class Order:
    """
    This class contains methods to be able to print the menu, grab inputs from user, calculates the bill,
    print the bill to console, and to print the bill on to an output file.
    """
    def __init__(self):
        """
        This method initializes the values of price_before_tax, price_after_tax, and tax to zero
        This method also grabs each burger item from class Burger and sets them as a separate variable to
        store them in a dictionary.
        """
        self._price_before_tax = 0
        self._price_after_tax = 0
        self._tax = 0
        self.DA = DA_Burger()
        self.BC = BC_Burger()
        self.MS = MS_Burger()
        self.WB = WB_Burger()
        self.DC = DC_Burger()
        self.burgers = [self.DA, self.BC, self.MS, self.WB, self.DC]

    def displayMenu(self):
        """
        Displays the menu of the Grill
        Prints the choices from 1-5 for the menu items and 6 to stop
        It grabs the menu items from the class Burger and uses its getters to find its name and price
        """
        print("\n----------- The Grill -----------")
        number = 0
        for i in range(len(self.burgers)):
            print("{0}. {1:15s} {2:8.2f}".format(number, self.burgers[i].get_name(), self.burgers[i].get_price()))
            number += 1
        print("6. Exit")

    def getInput(self):
        """
        This method takes the burgers initialized in the __init__ method and gives it a quantity by asking
        what the person ordering wants and how many of that item they want.
        It starts by asking user to input the first item they want and then the user sets that items quantity.
        """
        flag1 = True
        while flag1:
            try:
                burger_choice = int(input("Enter a choice from 1-5 to order something from the menu, 6 to quit: \n"))
                if burger_choice < 1 or burger_choice > 6:
                    print("Error! Please enter a value from 1-6 only please!")
                elif burger_choice == 6:
                    flag1 = False
                else:
                    flag2 = True
                    while flag2:
                        try:
                            number = int(input("Enter the quantity you want:\n"))
                            if number <= 0:
                                print("Error! Please enter a positive integer only!")
                            else:
                                flag2 = False
                        except:
                            print("Error! Please try again!")
                    self.burgers[burger_choice - 1].set_quantity(number)
            except:
                print("Error! Please enter integers only!")

    def calculate(self):
        """
        This method calculates the total price of the order by getting the quantity of each burger in the order
        and multiples it by the price of each menu item. The method them multiplies the total price of order by the
        tax if the person ordering is a staff member.
        """
        job = int(input("Are you student or staff? \nEnter 1 for student and 2 for staff: \n"))
        if job == 2:
            self._tax = 0.09
        for i in range(len(self.burgers)):
            self._price_before_tax += self.burgers[i].get_price() * self.burgers[i].get_quantity()
            self._price_after_tax = self._price_before_tax + (self._price_before_tax * self._tax)

    def print_bill(self):
        """
        This method takes everything from the class Order to be able to print the bill out on the console.
        It takes burgers from the __init__(self) method and the setters and getters from the class Burger
        to be able to get the prices and quantities of each burger.
        """
        print("Your bill: \n")
        for i in range(len(self.burgers)):
            print(" %-20s Qty: %-10d Price: $%-10.2f Total: $%-10.2f" %
                  (self.burgers[i].get_name(), self.burgers[i].get_quantity(), self.burgers[i].get_price(),
                   (self.burgers[i].get_price() * self.burgers[i].get_quantity())))
        print("-" * 50)
        print("Price before the tax was applied: ", round(self._price_before_tax, 2))
        print("Price after tax was applied: ", round(self._price_after_tax, 2))

    def saveToFile(self):
        """
        This method uses import time and import datetime to save the output file in position of year,month,date
        and then the hour( in 24 hour time), minutes and seconds.
        The method also takes everything from the class Order and prints out the bill in the output file
        """
        timeStamp = time.time()
        orderTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H-%M-%S')
        orderTimeStamp = orderTimeStamp + '.txt'
        with open(orderTimeStamp, 'w') as fileHandleToSaveTheBill:
            fileHandleToSaveTheBill.write("Your bill:\n")
            for i in range(len(self.burgers)):
                fileHandleToSaveTheBill.write(" %-20s Qty: %-10d Price: $%-10.2f Total: $%-10.2f" %
                                              (self.burgers[i].get_name(), self.burgers[i].get_quantity(),
                                               self.burgers[i].get_price(),
                                               (self.burgers[i].get_price() * self.burgers[i].get_quantity())) + '\n')
            fileHandleToSaveTheBill.write("-" * 50 + '\n')
            fileHandleToSaveTheBill.write("Price before tax:  $" + str(round(self._price_before_tax, 2)) + '\n')
            fileHandleToSaveTheBill.write("Price after tax:  $" + str(round(self._price_after_tax, 2)) + '\n')
