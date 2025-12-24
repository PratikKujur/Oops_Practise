"""
Create a class called Order which stores item and its prices
Use Dunder function __gt__() to convey that:
    order1>order2 if price of order1> price of order2
"""

class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    
    def __gt__(self,order_):
        return self.price>order_.price
            

o1=order("melton bottole",999)
o2=order("cello bottle",899)

print(o1>o2)

