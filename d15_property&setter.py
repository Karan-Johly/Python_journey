class Sample:

    def __init__(self,mkval):
        self.val=mkval
    @property
    def val(self):
        return self.__val
    @val.setter
    def val(self,pval):
        self.__val=pval

S = Sample(20)
S.val=100
print(S.val)
