square_meters_total = float(input())
price_per_square_meter = 7.61
price = square_meters_total * price_per_square_meter
discount = price * 0.18
discounted_price = price - discount

print(f'The final price is: {discounted_price} lv.')
print(f'The discount is: {discount} lv.')
