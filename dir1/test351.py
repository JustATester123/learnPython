def add(a,b):
    print(a+b)
    return a+b

c=add(1,2)

print(c)

def add(a=1,b =5):
    return a+b

print(add())
print(add(3,5))