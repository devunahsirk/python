try:
    num=int(input("Enter numerator"))
    den=int(input("Enter denominator"))
    result=num/den
    print(result)   

except ZeroDivisionError as e:
    print(e)
    print("Do not enter zero duhh")
except ValueError as e:
    print(e)
    print("enter a numbr duhh")
except Exception as e:
    print(e)
    print("Something went wrong that is not known, check again")
finally:
    print("I am done try again")            