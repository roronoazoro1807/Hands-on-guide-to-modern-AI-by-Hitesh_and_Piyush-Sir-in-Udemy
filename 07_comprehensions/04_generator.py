daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = sum(sale for sale in daily_sales if sale > 5)
print("Total cups (sales > 5):", total_cups)

max_sale = max(sale for sale in daily_sales if sale > 5)
print("Maximum sale (above 5):", max_sale)

min_sale = min(sale for sale in daily_sales if sale > 5)
print("Minimum sale (above 5):", min_sale)

high_demand = any(sale > 12 for sale in daily_sales)
print("High demand day (>12 cups)?", high_demand)

consistent_sales = all(sale > 2 for sale in daily_sales)
print("All days >2 cups?", consistent_sales)

filtered_sales = list(sale for sale in daily_sales if sale > 5)
print("Filtered sales (list):", filtered_sales)
