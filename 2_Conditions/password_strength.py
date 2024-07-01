password = input("Enter your password:")
password_length=len(password)

if len(password) < 6:
    Strength = "Weak"
elif len(password) <= 10:
    Strength = "Medium"
else:
    Strength = "Strong"

print("THe password is:",Strength)