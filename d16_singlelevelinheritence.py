        # Single Inheritence

class dost1:
    pen="Parker"
class dost2(dost1):
    pencil="Nataraj"

    def use(self):
        print(self.pen)
        print(self.pencil)

d2=dost2()
d2.use()