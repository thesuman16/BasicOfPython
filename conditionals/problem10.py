# pet food recommendation
#recommend a pet food based on the pet's species & age : Dog <2 yers - Puppy Food, Cat: >5years - milk

pet = input("enter pet name (Dog/ Cat): ")
age = int(input("Enter age: "))

if pet == "Cat":
    if age > 5:
        print("milk")
else:
    print("Consult Doctor")

    
if pet == "Dog":
    if age <4:
        print("Puppy Food")
else:
    print("Consult Doctor")