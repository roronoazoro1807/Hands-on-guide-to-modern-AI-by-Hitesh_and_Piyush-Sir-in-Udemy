class ChaiOrder:
    def __init__(self, type_, size):
        # Instance attributes (unique to each object)
        # using type_ (with underscore) because "type" is a built-in function in Python
        self.type = type_
        self.size = size

    def summary(self):
        # Instance method → uses self to access attributes of that specific object
        return f"{self.size}ml of {self.type} Chai."


# Creating first object → constructor (__init__) runs automatically
order = ChaiOrder("Ginger", 200)
print(order.summary())

# Creating second object
order_two = ChaiOrder("Masala", 180)
print(order_two.summary())
