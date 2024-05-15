# Transport mode selection
# Chose a mode of transportation based on distance <3km = walk, 3-15 =  bike, >15 = car

distance = int(input("Enter your Distance: "))

if distance <3:
    transport = "walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"
    
print("We recomend you the transport of: ", transport)