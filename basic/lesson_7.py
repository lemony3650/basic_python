# json
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = "text_file/numbers.json"
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)                 # 将Python对象编码成JSON字符串

with open(filename) as file_object:
    nums = json.load(file_object)                   # 将已编码的 JSON 字符串解码为 Python 对象
print(nums)


# 将数据加载到一个列表中
import json
import pygal
import math
from itertools import groupby

filename = 'text_file/btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)  # 1

# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))  # 1
    print("{} is month {} week {}, {}, the close price is {} RMB".format(
        date, month, week, weekday, close))

# 创建5个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []
# 每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)  # ①
line_chart.title = '比特币收盘价（¥）'
line_chart.x_labels = dates
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]  # ②
line_chart.add('收盘价', close)
line_chart.render_to_file('比特币收盘价折线图（¥）.svg')


line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '比特币收盘价对数变换（¥）'
line_chart.x_labels = dates
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]  # ①
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('比特币收盘价对数变换折线图（¥）.svg')
line_chart

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):  # 2
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])  # 3
    x_unique, y_mean = [*zip(*xy_map)]  # 4
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart


idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(
    months[:idx_month], close[:idx_month], '比特币收盘价月日均值（¥）', '月日均值')
line_chart_month


idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(
    weeks[1:idx_week], close[1:idx_week], '比特币收盘价周日均值（¥）', '周日均值')
line_chart_week


idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday',
      'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(
    weekdays_int, close[1:idx_week], '比特币收盘价星期均值（¥）', '星期均值')
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('比特币收盘价星期均值（¥）.svg')
line_chart_weekday


with open('比特币收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write(
        '<html><head><title>比特币收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
            '比特币收盘价折线图（¥）.svg', '比特币收盘价对数变换折线图（¥）.svg', '比特币收盘价月日均值（¥）.svg',
            '比特币收盘价周日均值（¥）.svg', '比特币收盘价星期均值（¥）.svg'
    ]:
        html_file.write(
            '    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))  # 1
    html_file.write('</body></html>')




# csv
import csv
# 添加日期
from datetime import datetime

filename = "text_file/sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)                                          # 建立连接关系，创建对象
    header_row = next(reader)                                       # 内置next 读取一行
    print(header_row)

    # for index, column_header in enumerate(header_row):              # enumerate 获取元素索引和值
    #     print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        try:                                                          # 异常处理，避免数据出现缺失或无法解析
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 可视化
from matplotlib import pyplot as plt

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs)
plt.plot(dates, lows, c='red')

plt.fill_between(dates, highs, lows, alpha=0.1)

plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
