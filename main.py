from order import *

if __name__ == "__main__":
    flag = True
    while flag:
        order = Order()
        order.displayMenu()
        order.getInput()
        order.calculate()
        order.print_bill()
        order.saveToFile()
        help(order)
        userInputToContinue = input("Continue for another order(Any keys= Yes, no= No)?\n")
        if userInputToContinue.lower() == 'no':
            print("The system is shutting down!")
            flag = False
        else:
            continue
"""
OUTPUT:
----------- De Anza Food Court -----------
1. De Anza Burger      5.25
2. Bacon Cheese        5.75
3. Mushroom Swiss      5.95
4. Western Burger      5.95
5. Don Cali Burger     5.95
6. Exit
Enter a choice from 1-5 to order something from the menu, 6 to quit: 
1
Enter the quantity you want:
5
Enter a choice from 1-5 to order something from the menu, 6 to quit: 
2
Enter the quantity you want:
5
Enter a choice from 1-5 to order something from the menu, 6 to quit: 
3
Enter the quantity you want:
5
Enter a choice from 1-5 to order something from the menu, 6 to quit: 
4
Enter the quantity you want:
5
Enter a choice from 1-5 to order something from the menu, 6 to quit: 
5
Enter the quantity you want:
5
Enter a choice from 1-5 to order something from the menu, 6 to quit: 
6
Are you student or staff? 
Enter 1 for student and 2 for staff: 
1
Your bill: 

 De Anza Burger       Qty: 5          Price: $5.25       Total: $26.25     
 Bacon Cheese         Qty: 5          Price: $5.75       Total: $28.75     
 Mushroom Swiss       Qty: 5          Price: $5.95       Total: $29.75     
 Western Burger       Qty: 5          Price: $5.95       Total: $29.75     
 Don Cali Burger      Qty: 5          Price: $5.95       Total: $29.75     
--------------------------------------------------
Price before the tax was applied:  144.25
Price after tax was applied:  144.25

Continue for another order(Any keys= Yes, no= No)?no
The system is shutting down!


----------- De Anza Food Court -----------
0. De Anza Burger      5.25
1. Bacon Cheese        5.75
2. Mushroom Swiss      5.95
3. Western Burger      5.95
4. Don Cali Burger     5.95
6. Exit
Enter a choice from 1-5 to order something from the menu, 6 to quit: 
7
Error! Please enter a value from 1-6 only please!
Enter a choice from 1-5 to order something from the menu, 6 to quit: 
5
Enter the quantity you want:
-9
Error! Please enter a positive integer only!
Enter the quantity you want:
10
Enter a choice from 1-5 to order something from the menu, 6 to quit: 
6
Are you student or staff? 
Enter 1 for student and 2 for staff: 
2
Your bill: 

 De Anza Burger       Qty: 0          Price: $5.25       Total: $0.00      
 Bacon Cheese         Qty: 0          Price: $5.75       Total: $0.00      
 Mushroom Swiss       Qty: 0          Price: $5.95       Total: $0.00      
 Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
 Don Cali Burger      Qty: 10         Price: $5.95       Total: $59.50     
--------------------------------------------------
Price before the tax was applied:  59.5
Price after tax was applied:  64.86
Help on Order in module order object:

class Order(builtins.object)
 |  This class contains methods to be able to print the menu, grab inputs from user, calculates the bill,
 |  print the bill to console, and to print the bill on to an output file.
 |  
 |  Methods defined here:
 |  
 |  __init__(self)
 |      This method initializes the values of price_before_tax, price_after_tax, and tax to zero
 |      This method also grabs each burger item from class Burger and sets them as a separate variable to
 |      store them in a dictionary.
 |  
 |  calculate(self)
 |      This method calculates the total price of the order by getting the quantity of each burger in the order
 |      and multiples it by the price of each menu item. The method them multiplies the total price of order by the
 |      tax if the person ordering is a staff member.
 |  
 |  displayMenu(self)
 |      Displays the menu of the De Anza Grill
 |      Prints the choices from 1-5 for the menu items and 6 to stop
 |      It grabs the menu items from the class Burger and uses its getters to find its name and price
 |  
 |  getInput(self)
 |      This method takes the burgers initialized in the __init__ method and gives it a quantity by asking
 |      what the person ordering wants and how many of that item they want.
 |      It starts by asking user to input the first item they want and then the user sets that items quantity.
 |  
 |  print_bill(self)
 |      This method takes everything from the class Order to be able to print the bill out on the console.
 |      It takes burgers from the __init__(self) method and the setters and getters from the class Burger
 |      to be able to get the prices and quantities of each burger.
 |  
 |  saveToFile(self)
 |      This method uses import time and import datetime to save the output file in position of year,month,date
 |      and then the hour( in 24 hour time), minutes and seconds.
 |      The method also takes everything from the class Order and prints out the bill in the output file
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

Continue for another order(Any keys= Yes, no= No)?yes

----------- De Anza Food Court -----------
0. De Anza Burger      5.25
1. Bacon Cheese        5.75
2. Mushroom Swiss      5.95
3. Western Burger      5.95
4. Don Cali Burger     5.95
6. Exit
Enter a choice from 1-5 to order something from the menu, 6 to quit: 
19
Error! Please enter a value from 1-6 only please!
Enter a choice from 1-5 to order something from the menu, 6 to quit: 
-2
Error! Please enter a value from 1-6 only please!
Enter a choice from 1-5 to order something from the menu, 6 to quit: 
2
Enter the quantity you want:
10
Enter a choice from 1-5 to order something from the menu, 6 to quit: 
6
Are you student or staff? 
Enter 1 for student and 2 for staff: 
2
Your bill: 

 De Anza Burger       Qty: 0          Price: $5.25       Total: $0.00      
 Bacon Cheese         Qty: 10         Price: $5.75       Total: $57.50     
 Mushroom Swiss       Qty: 0          Price: $5.95       Total: $0.00      
 Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
 Don Cali Burger      Qty: 0          Price: $5.95       Total: $0.00      
--------------------------------------------------
Price before the tax was applied:  57.5
Price after tax was applied:  62.67
Help on Order in module order object:

class Order(builtins.object)
 |  This class contains methods to be able to print the menu, grab inputs from user, calculates the bill,
 |  print the bill to console, and to print the bill on to an output file.
 |  
 |  Methods defined here:
 |  
 |  __init__(self)
 |      This method initializes the values of price_before_tax, price_after_tax, and tax to zero
 |      This method also grabs each burger item from class Burger and sets them as a separate variable to
 |      store them in a dictionary.
 |  
 |  calculate(self)
 |      This method calculates the total price of the order by getting the quantity of each burger in the order
 |      and multiples it by the price of each menu item. The method them multiplies the total price of order by the
 |      tax if the person ordering is a staff member.
 |  
 |  displayMenu(self)
 |      Displays the menu of the De Anza Grill
 |      Prints the choices from 1-5 for the menu items and 6 to stop
 |      It grabs the menu items from the class Burger and uses its getters to find its name and price
 |  
 |  getInput(self)
 |      This method takes the burgers initialized in the __init__ method and gives it a quantity by asking
 |      what the person ordering wants and how many of that item they want.
 |      It starts by asking user to input the first item they want and then the user sets that items quantity.
 |  
 |  print_bill(self)
 |      This method takes everything from the class Order to be able to print the bill out on the console.
 |      It takes burgers from the __init__(self) method and the setters and getters from the class Burger
 |      to be able to get the prices and quantities of each burger.
 |  
 |  saveToFile(self)
 |      This method uses import time and import datetime to save the output file in position of year,month,date
 |      and then the hour( in 24 hour time), minutes and seconds.
 |      The method also takes everything from the class Order and prints out the bill in the output file
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

Continue for another order(Any keys= Yes, no= No)?no
The system is shutting down!

Process finished with exit code 0

"""
