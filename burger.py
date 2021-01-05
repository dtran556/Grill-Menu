class Burger:
    """
    This class holds the methods and subclasses used in class Order to get the names and prices of each menu items
    and sets the quantity of each item.
    """
    def __init__(self, name = '', price = 0.00, quantity = 0):
        """
        This method sets name,price and quantity as instance cariables of the class so that they can be used by
        the other classes/subclasses.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return self.name + str(self.price) + str(self.quantity)
    def get_name(self):
        """
        This method gets the name of the menu item and returns the name of it.
        """
        return self.name
    def get_price(self):
        """
        This method gets the price of the menu item and returns its price.
        """
        return self.price
    def get_quantity(self):
        """
        This method gets the quantity of the menu item that the user wants to order and returns the quantity.
        """
        return self.quantity
    def set_quantity(self, quantity):
        """
        This method grabs the quantity and sets it in the variable quantity.
        """
        self.quantity = quantity

class DA_Burger(Burger):
    """
    This class is a subclass of the class Burger it takes the name, price and quantity and overrides them from the
    class Burger
    """
    def __init__(self):
        """
        This method overrides name, price, and quantity from the class Burger for the burger named De Anza Burger
        """
        super().__init__()
        self.name = 'De Anza Burger'
        self.price = 5.25
        self.quantity = 0

class BC_Burger(Burger):
    """
    This class is a subclass of the class Burger it takes the name, price and quantity and overrides them from the
    class Burger
    """
    def __init__(self):
        """
        This method overrides the name,price,and quantity for the burger Bacon Cheese from the class Burger.
        """
        super().__init__()
        self.name = 'Bacon Cheese'
        self.price = 5.75
        self.quantity = 0

class MS_Burger(Burger):
    """
    This class is a subclass of the class Burger it takes the name, price and quantity and overrides them from the
    class Burger
    """
    def __init__(self):
        """
        This method overrides the name, price, and quantity for the burger Mushroom Swiss from the class Burger
        """
        super().__init__()
        self.name = 'Mushroom Swiss'
        self.price = 5.95
        self.quantity = 0

class WB_Burger(Burger):
    """
    This class is a subclass of the class Burger it takes the name, price and quantity and overrides them from the
    class Burger
    """
    def __init__(self):
        """
        This method overrides the name, price, and quantity for the burger Western Burger from the class Burger
        """
        super().__init__()
        self.name = 'Western Burger'
        self.price = 5.95
        self.quantity = 0

class DC_Burger(Burger):
    """
    This class is a subclass of the class Burger it takes the name, price and quantity and overrides them from the
    class Burger
    """
    def __init__(self):
        """
        This method overrides the name, price, and quantity for the burger Don Cali from the class Burger
        """
        super().__init__()
        self.name = 'Don Cali Burger'
        self.price = 5.95
        self.quantity = 0


