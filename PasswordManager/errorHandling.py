height = int(input("height: "))
weight = int(input("weight: "))

bmi = weight / height ** 2

if height > 3:
    raise ValueError("Human height should not be over 3 meter")
else:
    print(bmi)