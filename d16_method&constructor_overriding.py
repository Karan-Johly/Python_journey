            # Method and Constructor overriding

class dost1:
    def __init__(self):
        print("Dost1 constructor")
    def use(self):
        print("Hello Dost1")

class dost2(dost1):
    def __init__(self):
        super().__init__()
        print("Dost2 constructor")
    def use(self):
        super().use()
        print("Hello dost2")
d2=dost2()