class addDict(dict):

    def __add__(self,other):
        self.update(other)
        return addDict(self)

a = {x:x*x for x in range(3) }
b = {4:1,5:2,6:45}
d1 = addDict(a)
d2 = addDict(b)
print (d1+d2)
print(a.update(b))
x = 2,1,
print(x)
