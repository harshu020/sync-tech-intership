weight= float(input("Enter weight in kg"))
height= float(input("Enter height in cm"))

height_in_meters = height / 100
bmi = weight / (height_in_meters ** 2)

print("Your BMI is:", bmi)

if bmi< 18.5:
    print("You're under weight")
elif 18.5 <= bmi <25:
    print("You're a normal weight")
else:
    print("You're over weight")
