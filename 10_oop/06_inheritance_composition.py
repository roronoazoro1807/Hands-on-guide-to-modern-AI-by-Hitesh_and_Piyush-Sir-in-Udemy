# -------------------------------
# Base / Parent Class
# -------------------------------
class BaseChai:
    def __init__(self, type_):
        self.type = type_  # instance attribute

    def prepare(self):
        print(f"Preparing {self.type} chai....")


# -------------------------------
# Child Class → inherits from BaseChai
# -------------------------------
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")


# -------------------------------
# Composition Example
# ChaiShop has-a Chai object
# -------------------------------
class ChaiShop:
    chai_cls = BaseChai  # default chai class (can be replaced by subclasses)

    def __init__(self):
        # composition: ChaiShop *contains* an instance of chai_cls
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()


# -------------------------------
# Inheritance + Composition
# FancyChaiShop inherits from ChaiShop
# -------------------------------
class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai  # overrides chai type used in the shop


# -------------------------------
# Create Objects
# -------------------------------
shop = ChaiShop()
fancy = FancyChaiShop()

# Using BaseChai
shop.serve()
# Output:
# Serving Regular chai in the shop
# Preparing Regular chai....

# Using MasalaChai (through inheritance override)
fancy.serve()
# Output:
# Serving Regular chai in the shop
# Preparing Regular chai....

# Child-specific method
fancy.chai.add_spices()
# Output:
# Adding cardamom, ginger, cloves.
