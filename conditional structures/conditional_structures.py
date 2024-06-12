def calculate_discount(price, discount_percent):
  # Convert discount percentage to a decimal (e.g., 20% becomes 0.2)
  discount = discount_percent / 100

  # Apply discount only if 20% or higher
  if discount >= 0.2:
    final_price = price * (1 - discount)  # Apply discount formula
  else:
    final_price = price  # No discount applied

  return final_price

# Get user input for original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage (0-100): "))

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price with a message
if discount_percent >= 0.2:
  print(f"Final price after applying {discount_percent:.2f}% discount: {final_price:.2f}")
else:
  print(f"No discount applied. Original price: ksh{original_price:.2f}")
