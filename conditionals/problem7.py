# coffe customization
# Customize a coffe order: small, medium or large with an option of extra shot of espresso.

order_size = input("Select Cofee size: Small/ Medium/ Large: ")
extra_shot = input('Extra shot ?\nlaEnter Yes (1)/ NO (0): ')

if extra_shot:
    coffe = order_size + " Cofee with an extra shot"
else:
    coffe = order_size + " Cofee"
    
print("Order: ", coffe)