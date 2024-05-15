#Movie tickets are priced based on age :
#₹120 for adults>18, ₹60 for children. If wednessday everyone gets ₹20 discoount


age = int (input("Provide me a age: "))
day = 'wednesday'

price = 120 if age >=18 else 60

if day == "wednesday":
    price = price - 20 #price -= 20

print("Ticket Price for you is ₹", price)