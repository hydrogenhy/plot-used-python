"""
绘制热力图代码。
常用于显示相关系数矩阵。
1.突出关键信息：热力图通过颜色的变化来突出数据的特征和差异，帮助我们快速发现数据中的规律和趋势。
2.可视化大规模数据：热力图适用于展示大规模数据矩阵，特别是在数据包含大量值时，热力图可以更好地展示数据的结构。
3.探索数据关联性：热力图可以帮助我们发现数据之间的关联性和相关性，尤其在探索多变量数据时特别有用。
4.色彩丰富：热力图的颜色映射可以选择多样，可以根据数据类型和需要选择合适的颜色映射，使得图像更美观和易读。
5.一目了然：热力图通过色彩的变化和色块的大小，可以在一张图中展示大量数据，让人一目了然。
6.强调差异：热力图的颜色变化可以有效地突出数据之间的差异和异常值，有助于快速定位问题。
"""
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换

# 生成示例数据（10x10的二维矩阵）
data = np.random.randint(1, 10, size=(10, 10))

# 创建一个Figure对象和一个子图
fig, ax = plt.subplots()

# 绘制热力图，并设置样式
heatmap = ax.imshow(data, cmap='hot', interpolation='nearest', aspect='auto')
'''
cmap参数设置：
'viridis'：从蓝色到黄色渐变，用于连续数据，特别适用于数据的渐变效果。
'plasma'：从紫色到橙色渐变，用于连续数据，较viridis颜色更丰富。
'inferno'：从黑色到黄色渐变，用于连续数据，较viridis颜色更加明亮。
'magma'：从黑色到白色渐变，用于连续数据，较viridis颜色更适合打印。
'cividis'：从蓝色到黄色渐变，用于连续数据，颜色较温和。
'cool'：从青色到蓝色渐变，用于连续数据，适用于冷色调的数据。
'hot'：从黑色到红色渐变，用于连续数据，适用于暖色调的数据。
'coolwarm'：从蓝色到红色渐变，用于连续数据，冷暖色调交替。
'rainbow'：七色彩虹渐变，用于连续数据，颜色多样。
'''
# 添加颜色条
cbar = plt.colorbar(heatmap, fraction=0.046, pad=0.04)

# 添加图例
ax.set_title('热力图', fontsize=16, fontweight='bold')

# 添加横纵坐标label
ax.set_xlabel('X轴', fontsize=14, fontweight='bold')
ax.set_ylabel('Y轴', fontsize=14, fontweight='bold')

# 设置颜色条标签字体大小
cbar.ax.tick_params(labelsize=12)

# 设置横纵坐标标签字体大小
ax.tick_params(axis='both', which='major', labelsize=12)

# 设置背景颜色
ax.set_facecolor('#f0f0f0')

# 设置图表边框颜色
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# 显示图形
plt.tight_layout()
plt.show()