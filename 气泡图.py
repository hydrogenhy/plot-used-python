"""
绘制气泡图的代码
甚至可以做有范围、权重的作图。如经典的信号覆盖问题。
1.强调气泡大小：气泡的大小代表第三个变量的数值，通过气泡的大小变化，突出数据的差异和趋势。
2.多变量对比：气泡图可以同时展示多个数据组，每个数据组的气泡大小和颜色可以代表不同的变量，有助于数据的对比和分析。
3.突出数据差异：气泡图通过气泡大小的变化，可以清晰地展示数据之间的差异和分布情况。
4.聚焦关键数据：气泡图的大小突出了数据的重要特征，有助于识别关键数据和异常值
"""
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换

# 生成示例数据
x = np.random.rand(50)  # 随机生成50个x坐标
y = np.random.rand(50)  # 随机生成50个y坐标
size = np.random.randint(100, 500, 50)  # 随机生成50个气泡的大小
color = np.random.rand(50)  # 随机生成50个气泡的颜色

# 创建一个Figure对象和一个子图
fig, ax = plt.subplots()

# 绘制气泡图
scatter = ax.scatter(x, y, s=size, c=color, cmap='coolwarm', alpha=0.7, edgecolors='k')

# 添加颜色条
cbar = plt.colorbar(scatter)

# 添加图例
ax.set_title('气泡图', fontsize=16, fontweight='bold')

# 添加横纵坐标label
ax.set_xlabel('X轴', fontsize=14, fontweight='bold')
ax.set_ylabel('Y轴', fontsize=14, fontweight='bold')

# 设置颜色条标签字体大小
cbar.ax.tick_params(labelsize=12)

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
