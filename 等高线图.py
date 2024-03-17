"""
绘制等高线图的代码
适用于地形、函数、场、势的绘制。
1.表现数据等值线：等高线图通过等值线来展示数据的分布情况，帮助人们快速了解数据的变化趋势和模式。
2.保留二维信息：等高线图是二维图形，能够清晰表达两个自变量之间的关系，适用于分析二维数据。
3.显示数据变化：等高线图通过等值线的间距和形态变化，能够有效显示数据的变化趋势和梯度。
4.强调变化梯度：等高线图通过等值线的密集程度和形态变化，突出数据变化的梯度，有助于识别变化的快慢和方向。
5.检测异常值：等高线图可以帮助我们发现数据中的异常值，因为异常值通常在等值线中表现为不规则的形状。
"""
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换

# 生成示例数据（二维数组）
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = X ** 2 - Y ** 2

# 创建一个Figure对象和一个子图
fig, ax = plt.subplots()

# 绘制等高线图，并设置样式
contour = ax.contour(X, Y, Z, levels=50, cmap='coolwarm', linewidths=1.5)

# 添加颜色条
cbar = plt.colorbar(contour, ax=ax)

# 添加图例
ax.set_title('等高线图', fontsize=16, fontweight='bold')

# 添加横纵坐标label
ax.set_xlabel('X轴', fontsize=14, fontweight='bold')
ax.set_ylabel('Y轴', fontsize=14, fontweight='bold')

# 设置颜色条标签字体大小
cbar.ax.tick_params(labelsize=12)

# 设置线条样式为虚线
for line in contour.collections:
    line.set_linestyle('dashed')

# 设置刻度标签字体大小
ax.tick_params(axis='both', which='major', labelsize=12)

# 设置背景颜色
ax.set_facecolor('#f0f0f0')

# 设置图表边框颜色
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# 显示图形
plt.tight_layout()
plt.show()
