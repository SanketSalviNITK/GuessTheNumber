import random

a=random.random()*10
b=int(a)

for x in range(3):
  c=int(input("Guess the number:"))
  if c==b:
    print("You Won")
    break
  else:
    print(2-x, " attemtps left, try again")
print("You Lose")
        
  