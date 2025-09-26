# Example 1: Passing immutable vs mutable objects
chai = [1, 2, 3]  # list is mutable


def edit_chai(cup):
    cup[1] = 42  # modifies the list in place


edit_chai(chai)
print(chai)  # Output: [1, 42, 3] → list changed because it's mutable


# -------------------------------
# Example 2: Positional vs Keyword arguments
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)


make_chai("Darjeeling", "Yes", "Low")  # Positional arguments
make_chai(
    tea="Green", sugar="Medium", milk="No"
)  # Keyword arguments (order doesn't matter)


# -------------------------------
# Example 3: Arbitrary arguments (*args, **kwargs)
def special_chai(*ingredients, **extras):
    # *ingredients → tuple of extra positional arguments
    # **extras → dict of extra keyword arguments
    print("Ingredients", ingredients)
    print("Extras", extras)


special_chai("Cinnamon", "Cardamom", sweetener="Honey", foam="yes")


# -------------------------------
# Example 4: Avoiding mutable default argument problem
# Using a list as default can cause data to persist across calls
def chai_order(order=None):
    if order is None:  # Create new list every time
        order = []
    print(order)


chai_order()  # Output: []
chai_order()  # Output: [] → does not retain previous call
