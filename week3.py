def calculate_discount(price,discount_price):
    if discount_percent>=20:
        new_price=price*(100-discount_percent)/100
        return new_price
    else:
        return price
    
    
price=float(input("Price: "))
discount_percent=float(input("Discount offered: "))
New=calculate_discount(price,discount_percent)
print(New)
