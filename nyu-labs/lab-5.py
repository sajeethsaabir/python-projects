print("Please enter your weight in pounds")
weight_in_pounds = int(input("Weight in pounds: "))

print("Please enter your height in inches")
height_in_inches = int(input("Height in inches: "))

weight_kgs = weight_in_pounds * 0.453592
height_m = height_in_inches * 0.0254

weight = round(weight_kgs, 1)
height = round(height_m, 1)

bmi = weight / (height ** 2)

Bmi = round(bmi, 1)

if Bmi < 18.5:
    print("Your BMI =", Bmi, "so your Weight Status is: Underweight")

elif 18.5 <= Bmi < 24.9:
    print("Your BMI =", Bmi, "so your Weight Status is: Normal")

elif 24.9 <= Bmi < 29.9:
    print("Your BMI =", Bmi, "so your Weight Status is: Overweight")

else:
    print("Your BMI =", Bmi, "so your Weight Status is: Obese")
