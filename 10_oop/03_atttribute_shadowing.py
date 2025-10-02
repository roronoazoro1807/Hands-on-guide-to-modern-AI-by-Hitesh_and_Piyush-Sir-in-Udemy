class Chai:
    temperature = "hot"  # class attribute
    strength = "Strong"


cutting = Chai()  # object created
print(cutting.temperature)  # "hot" → comes from class (no instance attr yet)

# --------------------------
cutting.temperature = "Mild"  # shadowing → creates an instance attr
cutting.cup = "small"  # instance attribute (not in class)
print("After changing ", cutting.temperature)  # "Mild" → instance wins
print("cup size is  ", cutting.cup)  # "small" → only object has it
print("Direct look into the class ", Chai.temperature)  # still "hot" in class

# --------------------------
del cutting.temperature  # deletes instance attr
# del cutting.cup            # this would delete instance attr 'cup'

print(cutting.temperature)  # "hot" → falls back to class attribute again
print(cutting.cup)  # "small" → still exists in object
