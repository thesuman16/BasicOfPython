# valided input
# Keep asking user for input until they enter a number betweeen 1 and 10

while True:
    num = int(input("Enter value between 1 and 10: "))
    if 1 <= num <= 10:
      print("Done")
      break
    else:
        print("Invalid number, try again.")