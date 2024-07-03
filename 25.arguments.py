#parameter will pack all argument in tuple

def sum(*arg):
    for i in arg:
        add=0
        add += i
    return add



print(sum(3,4,5))

