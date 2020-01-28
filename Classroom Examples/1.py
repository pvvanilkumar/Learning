name = input("pl. enter your name")
height = float(input("Pl. enter your height in meters"))
weight = int(input("Pl. enter your weight in KGs"))

bmi = weight/ height ** 2

print(" Hi {} your bmi is {}".format(name,round(bmi,2)))


