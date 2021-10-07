class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breath(self):
        print("I inhale,\n I exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print(" i move under water")

    def breath(self):
        super().breath()
        print("I do mine underwater")

nemo = Fish()
nemo.breath()

######### Slicing #########
"""its used to reduce o slicce trough a list or turple in python, it make working with lst and turple easier by just usin some sets of squre bracket and calling the index that we want to get hold of, we specify the begining, the end and the skip between them by using just collon (:) between them, see example below
 piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
 print(piano_keys[2 (the beginning of the slice) : 4(end of slice) : 2(ratio of slice)
 """