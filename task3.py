weight = float(input("Enter weight: "))
height = float(input("Enter height: "))
bmi = weight / (height * height)
print(bmi)
if bmi < 18.5:
    print("Category: Underweight")
elif  bmi > 18.5 and bmi < 24.9:
    print("Category: Normal Weight")
elif bmi > 25 and bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")


