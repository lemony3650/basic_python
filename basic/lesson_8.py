import matplotlib.pyplot as plt

# 折线图
squares = [1, 4, 9, 16, 25]

# 线粗
plt.plot(squares, linewidth=5)

# 提供x轴y轴参数输入输出 input_value = [1, 2, 3, 4, 5]
# plt.plot(input_value, squares, linewidth=5)

# 设置标题、轴标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.show()

# 散点图
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

# 大数
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40)
plt.axis([0, 1100, 0, 1100000])
# plt.show()

# 自动保存图表
plt.savefig('text_file/squares_plot.png', bbox_inches='tight')


# 直方图
# 产生数据
from random import randint

class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

die = Die()
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
# 可视化
import pygal
hist = pygal.Bar()

x_values = [1, 2, 3, 4, 5, 6]

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = x_values
hist.x_title = "Result"
hist.y_title = "Fequency of Result"

hist.add('D6', frequencies)
hist.render_to_file("text_file/die_visual.svg")
