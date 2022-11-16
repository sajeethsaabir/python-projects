print("Please enter your weight in pounds")
weight_in_pounds = int(input("Weight in pounds: "))

print("Please enter your height in inches")
height_in_inches = int(input("Height in inches: "))

weight_kgs = weight_in_pounds * 0.453592
height_m = height_in_inches * 0.0254

bmi = weight_kgs / (height_m ** 2)

print("Your BMI =", bmi)
