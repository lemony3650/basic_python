# 函数

# 关键字实参
# 默认值，必须先列出没有默认值的形参
def describe_pet(pet_type, name):
    print(pet_type)
    print(name)
    return name.title()

describe_pet(pet_type='dog', name='harry')


# 形参中传入列表永久修改   添加[:]传入副本而不影响列表本身
# *p 传入多个参数，用元组表示
def make_pizza(size, *toppings):
    print("\nMaking a pizza... " + str(size))
    for topping in toppings:
        print("\t-" + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'pepperoni', 'green peppers', 'extra cheese')

# 键值对存储多个任意参数
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v

    return  profile

user_profile = build_profile('a', 'b', location='princeton', field='physics')
print(user_profile)
