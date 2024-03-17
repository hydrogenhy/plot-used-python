"""
绘制直方图的代码。
1.简单直观：直方图是一种简单直观的图表类型，不需要复杂的数学知识就能理解数据的分布情况。
2.大数据适用：直方图适用于大量数据的可视化。对于大数据集，直方图可以帮助我们更好地理解数据的总体分布和趋势。
3.强调整体特征：直方图可以清楚地展示数据的整体特征，帮助我们发现数据中的规律和趋势。
4.无偏性：直方图不受数据的排序和个数的影响，对数据的表现是无偏的。
5.直观比较：直方图可以用来比较不同数据集或不同组别之间的差异，通过颜色或图案样式的设置，直观地显示数据之间的比较结果。
6.数据离散化：直方图将连续数据分组成离散区间，有助于对数据进行简化和归纳，更容易理解数据的结构。
7.显示数据分布：直方图能够直观地展示数据在不同区间的分布情况，帮助我们了解数据的集中程度、分散程度和峰值等特征。
"""
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换

# 生成示例数据
np.random.seed(0)
data1 = np.random.normal(0, 1, 100)

# 创建一个Figure对象和一个子图
fig, ax = plt.subplots()

# 设置直方图的边界和颜色
bins = 20
colors = ['g']

# 绘制直方图
ax.hist(data1, bins=bins, color=colors[0],  hatch='/', alpha=0.7, label='Group', edgecolor='black')

# 添加图例
ax.legend()

# 添加横纵坐标label
ax.set_xlabel('数值', fontsize=12)
ax.set_ylabel('频数', fontsize=12)

# 设置图表标题
ax.set_title('直方图', fontsize=14)

# 设置刻度标签字体大小
ax.tick_params(axis='both', which='major', labelsize=10)

# 添加网格线
# ax.grid(True, linestyle='--', alpha=0.7)

# 设置背景颜色
ax.set_facecolor('#f0f0f0')

# 设置图表边框颜色
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# 显示图形
plt.tight_layout()
plt.show()