# Student Name:   Paul Nicolli
# Student Number: 1037974

# INSERT YOUR ANSWER BELOW
# --------------------------
name = input("What is your name? ")
height = float(input("What is your height (m)? "))
weight = float(input("What is your weight (kg)? "))

# calculate BMI (weight / height*height )
bmi = (weight / (height*height))

# print output of BMI (and format to 1 decimal place)
print(f"Hi {name}, your BMI is: {bmi:.1f}")

