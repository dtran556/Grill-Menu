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
