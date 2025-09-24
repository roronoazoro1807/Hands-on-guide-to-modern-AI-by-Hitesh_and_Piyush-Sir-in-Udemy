# Function definition with parameters
# 'name' and 'chai_type' are PARAMETERS (placeholders for input values)
def print_order(name, chai_type):
    # Function body: defines what the function will do
    print(f"{name} ordered {chai_type} chai!")


# Function calls with actual values
# "Aman", "Hitesh", "Jia" and chai types are ARGUMENTS (real data passed to parameters)

print_order("Aman", "masala")  # 'name' = Aman, 'chai_type' = masala
print_order("Hitesh", "Ginger")  # 'name' = Hitesh, 'chai_type' = Ginger
print_order("Jia", "Tulsi")  # 'name' = Jia, 'chai_type' = Tulsi
