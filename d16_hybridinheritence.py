        # Hybrid Inheritence

class F:
    f="class F"
class G:
    g="class G"
class E(F,G):
    e="class E"
    # @property
    def use(self):
        print(self.e)
        print(self.g)
        print(self.f)
class B(F):
    b="class B"
class A(B):
    a="class A"
    # @property
    def use1(self):
        print("In class A")
        print(self.a)
        print(self.b)
        print(self.f)
class C(B):
    c="class C"
    # @property
    def use2(self):
        print("In class C")
        print(self.c)
        print(self.b)
        print(self.f)

obj1=E()
obj2=A()
obj3=C()

obj1.use()
print()
obj2.use1()
print()
obj3.use2()
print()