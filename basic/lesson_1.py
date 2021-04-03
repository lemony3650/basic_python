# 数字运算符
value = 3 ** 2      # 乘方运算
print(value)
value = 0.2 + 0.1
print(value)        # 浮点数运算  向后保留十多位

# 字符串大小写输出
age = 23
ss = str(age)           # 非字符串字符转换
name = 'ada lovelace'
print(name.title())     # title 首字母大写
print(name.upper())
print(name.lower())

# 去除字符串中的空格符，开头或者末尾
msg = ' python '
print(msg)
print(msg.lstrip())     # 临时变量 去除开头的空白
print(msg.rstrip())     # 临时变量 去除末尾的空白
print(msg.strip())      # 同时删除

# split()以空格分词
title = "alice in wonderland"
words = title.split()       # 列表形式
print(words)

# 用户输入输出
# 输入文本
message = input("tell me your input word: ")
print(message)

# 输入超过一行时
prompt = "If you tell us who are you, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(name)

# 输入转换为数值 int
age = int(input("your age"))
if age == 18:
    print("good")

# 文件读取和写入 r w a r+

# 路径 默认路径与可执行文件保持一致 linux / windows \
# 相对路径都可以用/         r
file_path = "text_file/word.txt"

with open(file_path) as file_object:           # with 自动选择关闭文件事件
    contents = file_object.read()              # read 读到文件末尾就会返回一个空字符串
    print(contents.rstrip())

with open(file_path) as file_object:
    for line in file_object:                    # line 读到末尾会有换行符 print也会换行
        print(line.rstrip())

with open(file_path) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# 文件写入
filename = "program.txt"

with open(filename, 'w') as file_object:
    file_object.write("do somethings...")

# 异常处理
try:
    print(5/0)
except ZeroDivisionError:
    print("informathins")
else:
    print("somethings...")
