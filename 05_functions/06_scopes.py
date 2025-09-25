# -------------------------------
# Example 1: Local vs Global Scope
# -------------------------------


def serve_chai():
    # 'chai_type' here is LOCAL to this function
    # Local variables exist only inside the function and shadow global variables
    chai_type = "Masala"
    print(f"Inside Function {chai_type}")  # Prints local 'Masala'


# Global variable
# Global variables exist throughout the module/script unless shadowed by a local variable
chai_type = "Lemon"

serve_chai()  # Calls the function → prints "Inside Function Masala"
print(f"Outside function {chai_type}")  # Prints global "Lemon"

# -------------------------------
# Example 2: Local, Enclosed, Global
# -------------------------------


def chai_counter():
    # Enclosing scope variable
    # Exists in the outer function and can be accessed by nested functions
    chai_order = "Lemon"

    def print_order():
        # Local scope inside inner function
        # Shadows the enclosing 'chai_order'
        chai_order = "Ginger"
        print("Inner Scope:", chai_order)  # Prints "Ginger" (local variable)

    print_order()  # Call inner function
    print("Outer:", chai_order)  # Prints enclosing variable "Lemon"


# Global variable
chai_order = "Tulsi"  # Global scope variable
chai_counter()  # Calls outer function → prints inner and outer scopes
print("Global:", chai_order)  # Prints global "Tulsi"

# -------------------------------
# Notes on Scope (LEGB)
# -------------------------------
# L → Local (inside function)
# E → Enclosed (outer function for nested functions)
# G → Global (top-level variable)
# B → Built-in (Python default functions like print(), len(), etc.)
