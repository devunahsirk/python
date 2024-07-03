temp =int(input("what is the temperature today?"))

if temp<30 and temp>0:
    print("The temperature is good today you can go outside")
elif temp<0 or temp>=30:
    print("The temperature is bad today dont go outside")
else:
    print("No idea about the weather today soorry")        