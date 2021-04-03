# 字典{}
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# 增加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

del alien_0['points']


# 同类型字典定义-结构体，最后一行加逗号，且右括号位置
favorite_languages = {
    'jen': 'python',
    'sarsh': 'c',
    'edward': 'ruby',
    }

for name in favorite_languages.keys():
    print(name.title())
for value in favorite_languages.values():
    print(value)

for name in sorted(favorite_languages.keys()):
    print(name.title())

# set 表示列表中的项独一无二
for language in set(favorite_languages.values()):
    print("not repeat value")

# 字典组成列表
aliens = []
for alien_number in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print(aliens)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)

# 字典中包含列表
pizza = {'crust': 'thick',
         'toppings': ['mushrooms', 'extra cheese'],
    }

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarsh': ['c', 'go'],
    'edward': ['ruby', 'c'],
    }
for name, languages in favorite_languages.items():
    print(name.title())
    for language in languages:
        print("\t" + language.title())

# 字典嵌套字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name)
    print("\tlocation: " + location)
