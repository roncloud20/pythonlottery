import random

lucky = []

for i in range(0,6):
    l = random.randint(1,10)
    if l in lucky:
        continue
    lucky.append(l)

print(lucky)
