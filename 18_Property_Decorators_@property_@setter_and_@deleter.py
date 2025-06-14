class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        print("Getting price...")
        return self.__price
    
    @price.setter
    def price(self, value):
        print("Setting price...")
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Price can't be negative")
        
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self.__price

product1 = Product(10)

print(product1.price)
product1.price = 150
print(product1.price)
del product1.price