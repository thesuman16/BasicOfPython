# Password strength Checker
#Check if weak, medium or strong. <6 = Weak, 6-10 = Medium, >10 chars = Strong

password = input("Enter your password : ")

if len(password) <6:
    strength = "Weak"
elif len(password) <=10:
    strength = "Medium"
else:
    strength = "Strong"
    
print("Password Strength is : ", strength)