        # Composition

class dost1:
    pen="Parker"
class dost2:
    pencil="Nataraj"

    def use(self):
        d1=dost1()
        print(d1.pen)
        print(self.pencil)

d2=dost2()
d2.use()