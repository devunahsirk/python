import random

x=random.randint(1,6)
print(x)

y=random.random()  #gives random number ebtn 0&1
print(str(y))

list=["rock","paper","scissor"]
z=random.choice(list)
print(z)

card=[1,2,3,4,5,"a","b","c","d"]
random.shuffle(card)
print(card)