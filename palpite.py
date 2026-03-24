import random

a1 = random.randint(1, 99)
r = random.uniform (1, 99)
value_adjustment = round(r, 1)

for i in range(3):
    print(f"Termo {i+1}: {a1+(i*value_adjustment)}")

while True:
    if value_adjustment == float(input("Find the correct ratio and submit your answer: ")):
        print("Congratulations, you wrote the correct aswer!")
        break
    else:
        print("Nop, try again.")
