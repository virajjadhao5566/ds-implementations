class Item:
    pay_rate = 0.8
    all = []
    # init works like a constructor
    def __init__(self,name:str,price:float,quantity=0):
        # Used for checking negative
        assert price >= 0, f"Price {price} is negative"
        assert quantity >= 0

        # Initialisation like this in cpp
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
    
    def calculatePrice(self):
        return self.price*self.quantity
    
    def addDiscount(self):
        self.price = self.price*self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}','{self.price }')"
    
item1 = Item("viraj",3,4)
item2 = Item("vira",3,4)
item3 = Item("vir",3,4)
print(item1.all) 
