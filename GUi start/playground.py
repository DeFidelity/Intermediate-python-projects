# we can get our function to have infinite num of input just by using the asteric and passing through a tupple when
# ever the function is called.

def add(*args):
    ans = 0
    print(args[0])
    for num in args:
        ans += num
    return ans
    # and even sisce its a tuple we can also get a specific value by calling it like this:


print(add(1, 2, 4, 3, 4, 5))


# and this unlimited argument are called unlimited positional argument.


# Key word argument  (**kwargs)

def calculate(n, **kwargs):
    # print(kwargs)
    # #to loop through kwargs, we do that as we do loop through dictonaries
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n -= kwargs["subtract"]


calculate(7, add=5, subtract=7)
# with kwargs we can easily create a class with keywords which more can be add to or
# more can be replaced there, example below

class Car():
    def __init__(self, **kw):
        self.color = kw.get("color")
        self.model = kw.get("model")
        self.make = kw.get("make")

my_car = Car(model= "G-wagon", color= "blue")
print(my_car.model, my_car.color, my_car.make)