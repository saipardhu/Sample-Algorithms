class A:
    def a(self):
        print("From A")
class B(A):
    def a(self):
        super(B, self).a( )
        print("From B")

b1= B()
b1.a()
#b1.b()