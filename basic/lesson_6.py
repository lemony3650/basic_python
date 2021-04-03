# 模块 类

def make_pizza(size, *toppings):
    print("\nMaking a pizza... " + str(size))
    for topping in toppings:
        print("\t-" + topping)


# lambda() map() reduce() filter()
def add(x):
    return x+2

f = lambda x: x + 2

a = [1, 2, 3]
b = [i+2 for i in a]

c = map(lambda x: x + 2, a)
c = list(c)

# 过滤
d = filter(lambda x: x > 5 and x < 8, range(10))
d = list(d)


# 类
class Dog():

    def __int__(self, name, age):
        self.name = name
        self.age = age
        self.type = 'dog'               # 指定默认参数

    def sit(self):
        print(self.name.title())

    def roll_over(self):
        print(self.name.title())

my_dog = Dog('while', 6)

class Battery():

    def __init__(self, battery_size=70):
        self.battery = battery_size


class TideDog(Dog):
    def __init__(self, name, age):
        super.__init__(name, age)
        self.newattri = 'tide'
        self.battery = Battery()            # 继承直接用
