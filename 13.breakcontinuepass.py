while True:
    name=input("Enter your name")
    if name !="":
        break

number= "7896-555-373"

for i in number:
    if i=="-":
        continue
    print(i,end="") #end is used to avoid printing in new line