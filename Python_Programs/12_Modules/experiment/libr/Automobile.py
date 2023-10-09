class Automobile:
    #Constructor
    def __init__(self,make,model,regno):
        #Instance attributes
        self._carmake = make
        self.carmodel = model
        self.carregno = regno

    @property
    def carmake(self):
        return self._carmake

    @carmake.getter
    def carmake(self):
        print("Returing {}".format(self.carmodel))
        return self._carmake

    @carmake.setter
    def carmake(self,carmake):
        print("Setting make to {}".format(carmake))
        self._carmake = carmake

    @carmake.deleter
    def carmake(self):
        print("Deleting {}....".format(self.carregno))
        del self._carmake