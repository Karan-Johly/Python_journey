class Sample:
    def __init__(self,val):
        self.val=val
    def get_val(self):
        return self.val
    def set_val(self,val):
        self.val=val

S = Sample(20)
print(S.get_val())
S.set_val(10)
print(S.get_val())