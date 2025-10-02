class Chaicup:
    size = 150  # class attribute

    def describe(self):  # instance method (needs self)
        return f"A {self.size} ml Chai Cup"


cup = Chaicup()  # create object
print(cup.describe())  #  Normal way: Python passes 'cup' as self
cup.size = 100  # shadowing: instance attribute created
print(Chaicup.describe(cup))  #  Equivalent manual call
