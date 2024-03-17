"""
绘制箱线图代码
1.易读易懂：箱线图是一种直观且易懂的图表类型，无需复杂的数学知识即可解读数据的分布情况。
2.高效展示信息：箱线图能够在一个图中展示出数据的多个统计特征，包括中位数、四分位数、最大值、最小值和离群值，简洁高效。
3.检测异常值：箱线图可以帮助我们发现数据中的异常值，从而进行数据清洗或者更深入的分析。
4.有效比较：箱线图可以同时展示多组数据的分布情况，有助于进行数据间的比较和对比。
5.无偏性：箱线图对数据的排序和数量不敏感，其表现是无偏的，适用于多种类型的数据。
"""
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换

# 生成示例数据
np.random.seed(0)
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(2, 1.5, 100)
data3 = np.random.normal(-2, 1.5, 100)
data4 = np.random.normal(3, 1, 100)
data5 = np.random.normal(-1, 0.5, 100)

# 创建一个Figure对象和一个子图
fig, ax = plt.subplots()

# 绘制箱线图
boxes = ax.boxplot([data1, data2, data3, data4, data5], labels=['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'],
                   sym='o', vert=True, patch_artist=True)

# 设置每组数据的颜色
colors = ['tab:blue', 'yellow', 'tab:green', 'tab:red', 'tab:purple']
for box, color in zip(boxes['boxes'], colors):
    box.set(facecolor=color)

# 添加图例
ax.legend(boxes['boxes'], ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'], loc='upper right')

# 添加横纵坐标label
ax.set_xlabel('组别', fontsize=12, fontweight='bold')
ax.set_ylabel('数值', fontsize=12, fontweight='bold')

# 设置图表标题
ax.set_title('箱线图', fontsize=14, fontweight='bold')

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
plt.tight_layout()
plt.show()
