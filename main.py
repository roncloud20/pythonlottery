import random


lucky = set()
while len(lucky) < 6:
    l = random.randint(1,10)
    lucky.add(l)
lucky = list(lucky)
print(lucky)# THis is the output
  
