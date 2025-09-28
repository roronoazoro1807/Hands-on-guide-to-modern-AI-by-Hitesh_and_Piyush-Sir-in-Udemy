# Create a dictionary of squares
squares = {x: x * x for x in range(6)}
print(squares)


tea_prices_inr = {"Masala": 50, "Green": 40, "Lemon": 200}

tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}

print(tea_prices_inr)
print(tea_prices_usd)
