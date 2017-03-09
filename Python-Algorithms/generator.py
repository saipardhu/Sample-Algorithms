def foo():
    for i in range(3):
        print("before val:" ,int(i))
        yield i
        #next()
        print("after val:" ,int(i))

if __name__== '__main__':
    f = foo()
    for i in range(3):
        next(f)



