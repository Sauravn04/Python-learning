distance = int(input("Enter the distance:"))

if distance < 3:
    mode = "Walk"
elif distance <= 15:
    mode = "Bike"
else:
    mode = "Car"
print("AI recommendes you the this mode of transport:",mode)