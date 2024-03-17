"""
绘制折线图的代码。
常用于绘制数据走势。用途广泛。
1.显示趋势和变化：折线图特别适合展示数据随时间或其他连续变量的趋势和变化。通过将数据点连接起来，折线图能够直观地显示出数据的走势和趋势，
  帮助人们更好地理解数据的演变过程。
2.强调数据关系：折线图可以同时展示多条折线，比较多组数据的变化情况。这样，我们可以很容易地发现数据之间的关联和差异。
3.易于比较：通过将多个数据系列放在同一张图中，折线图提供了一个很好的比较方式。这样，我们可以很快地看出不同数据之间的差异，而不需要进行复杂的数据分析。
4.可视化异常和变动：折线图对于数据的异常值和波动有很好的反应，让人们快速识别出数据的特殊点。
5.显示周期性：如果数据具有明显的周期性变化，例如季节性或周期性，折线图能够清晰地表现这种特征。
6.突出重点：折线图可以突出数据的特定部分或重点，帮助观众关注关键的数据变化。
7.直观易懂：折线图简单直观，不需要高级的数据解读技巧。即使对于非专业人员，也可以很容易地理解数据的变化趋势。
"""
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换
# 数据示例，假设有五条折线，每条折线有5个数据点
y1 = [2, 4, 1, 5, 2]
y2 = [1, 3, 2, 3, 4]
y3 = [3, 1, 3, 2, 5]
y4 = [4, 2, 3, 1, 3]
y5 = [2, 3, 4, 2, 1]
x = [i for i in range(len(y1))]

# 创建一个Figure对象和一个子图
fig, ax = plt.subplots()

# 设置折线的线条样式、颜色和标签
line_styles = ['-', '--', ':', '-.', 'dashdot']
# 线条样式有'-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
line_colors = ['b', 'g', 'r', 'y', 'black']  # 这是线条颜色，也可以用'#123456'来表示
line_labels = ['Line 1', 'Line 2', 'Line 3', 'Line 4', 'Line 5']  # 这是图例名称
line_widths = [1.5, 2.0, 2.5, 1.0, 1.5]  # 调整线条粗细的参数
for i in range(5):
    ax.plot(x, globals()[f'y{i+1}'], linestyle=line_styles[i], color=line_colors[i], label=line_labels[i], linewidth=line_widths[i])

# 添加具体数值
for i in range(len(x)):
    ax.annotate(f'{y1[i]}', (x[i], y1[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# 添加图例
ax.legend()

# 添加横纵坐标label
ax.set_xlabel('X轴', fontsize=12)
ax.set_ylabel('Y轴', fontsize=12)

# 设置图表标题
ax.set_title('折线图', fontsize=16, fontweight='bold')

# 设置刻度标签字体大小
ax.tick_params(axis='both', which='major', labelsize=10)

# 添加网格线
ax.grid(True, linestyle='--', alpha=0.7)

# 设置背景颜色
ax.set_facecolor('#f0f0f0')

# 设置图表边框颜色
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# 显示图形
plt.show()

'''
# 绘制置信区间
import matplotlib.pyplot as plt
import numpy as np

# 示例数据
x = np.linspace(0, 10, 100)
y = np.sin(x)
confidence_interval = 0.2  # Example confidence interval value
upper_bound = y + confidence_interval
lower_bound = y - confidence_interval

# 创建一个Figure对象和一个子图
plt.figure(figsize=(10, 6))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Confidence Intervals')

# 绘制线条
plt.plot(x, y, label='Data', color='blue')

# 置信区间填颜色
plt.fill_between(x, lower_bound, upper_bound, color='lightblue', alpha=0.5, label='Confidence Interval')

# 添加图例
plt.legend()

# 显示图形
plt.show()
'''