        # Multiple Inheritence

class dost1:
    pen="Parker"
class dost2:
    pencil="Nataraj"
class dost3(dost1,dost2):
    eraser="Sensil"
    def use(self):
        print(self.pen)
        print(self.pencil)
        print(self.eraser)

d3=dost3()
d3.use()