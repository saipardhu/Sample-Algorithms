def add(a,b):
    return a+b
def mul(func, a,b):
    c = func(a,b)
    print(c*a*b)
mul(add,1,2)

def sample():
    print("Hey")

def dec(func):
    print("I'm from dec")
    func()

dec(sample)
# dec(sample())


