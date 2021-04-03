# 列表list []  元组tuple ()
# 类似二维数组，可以方便存放不同类型的数据格式

bicycles = ['teck', 'cannondale', 'redline', 'specialized']
motorcycles = []

print(bicycles)         # 会以列表的形式输出，包括括号和引号
print(bicycles[0].title())
print(bicycles[-1])     # 访问最后一个元素时，采用-1下标号，为空时返回错误
len(bicycles)           # 列表长度

# append count index inset pop
# 添加元素
bicycles.append('ducati')           # 追加方式
print(bicycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
print(motorcycles)
motorcycles.insert(0, 'ducati')      # 插入方式
print(motorcycles)

# 删除元素
del motorcycles[0]                   # 删除元素del
print(motorcycles)

# 出栈方式删除
motorcycles = ['honda', 'yamaha', 'suzuki']
poped_motorcycles = motorcycles.pop()
print(motorcycles)
print(poped_motorcycles)
poped_first = motorcycles.pop(0)    # 指定出栈位置

# 按照值删除
motorcycles.remove('yamaha')        # 只能删除第一个指定的值

# 列表排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()                         # 内部永久排序
cars.sort(reverse=True)             # 反序
cars.reverse()                      # 永久倒置

# 临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(sorted(cars, reverse=True))


# 数字列表
for value in range(1, 5):               # range() 生成数字 1-4
    print(value)

for value in range(1, 11, 2):           # range() 指定步长2
    print(value)

numbers = list(range(1, 11))            # list生成列表
print(numbers)

squares = [value**2 for value in range(1, 5)]            # 生成列表
print(squares)

# 统计计算列表
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:3])
print(players[1:])

print(players[-3:])                 # 输出最后三个元素

# 切片复制
my_foods = ['pizza', 'falafel', 'carrpt cake']
friend_food = my_foods              # 只是指向了同一个内存，并不是复制副本

friend_foods = my_foods[:]          # 整个列表复制
print(my_foods)
print(friend_foods)


# 元组()

# 不可变的列表，不能修改里面的值
dimensions = (200, 20)
print(dimensions[0])
print(dimensions[1])

# 但能够对元组重新赋值
dimensions = (400, 20)
