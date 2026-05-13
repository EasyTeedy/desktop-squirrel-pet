def lolroffel(age, sex):
    if sex == "male":
        max_hr_bpm = 223 -0.9*age
    elif sex == "female":
        max_hr_bpm = 226 - 1.0*age
    else:
        max_hr_bpm = 220 - age
    return round(max_hr_bpm)

input_age = int(input("Enter your age: "))
input_sex = input("Enter your sex (male/female): ")

lolroffel_result = lolroffel(input_age, input_sex)
print(f"Your estimated maximum heart rate is: {lolroffel_result} bpm")