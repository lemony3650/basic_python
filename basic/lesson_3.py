# 遍历循环

# for  缩进后的为代码块，全部执行
magicians = ['alice', 'david', 'carolina']
for var in magicians:
    print(var.title() + ", that was a great trick!")
    print("...\n")
print("over!")

# 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[0:3]:
    print(player.title())

# 遍历字典
favorite_languages = {
    'jen': 'python',
    'sarsh': 'c',
    'edward': 'ruby',
    }

for key, value in favorite_languages.items():
    print("\nKey: " + key)
    print("Value: " + value)

for name in favorite_languages.keys():          # keys()返回一个列表
    print(name.title())

if 'erin' not in favorite_languages.keys():
    print("do somethings...")

# while
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 条件语句 and | or | in | not in
# break continue
age = 19
if age <= 18:
    print("something")
elif age <= 30:
    print("somethings")
else:
    print("do something")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni']
request_toppings = ['mushrooms', 'french fries', 'extra cheese']

for request_topping in request_toppings:
    if request_topping in available_toppings:
        print("do somethings")
    else:
        print("somethings")
