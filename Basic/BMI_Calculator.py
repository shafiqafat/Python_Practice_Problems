weight = float(input("Enter Your Weight(In Kg): "))
height = float(input("Enter Your Height(in Meter): "))

bmi = float(weight/height**2)
print("BMI: ",round(bmi, 2))
if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
