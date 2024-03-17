"""
3D柱状图绘制代码
"""
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换

# 示例数据
x = [1, 2, 3]
y = [1, 2, 3, 4, 5]
z = [
    [5, 4, 2],
    [7, 6, 3],
    [7, 5, 4],
    [6, 7, 3],
    [5, 6, 2]
]

# 创建3D图形对象
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制三维柱状图
dx = dy = 0.5  # 设置柱子的宽度
dz = [row[0] for row in z]  # 设置柱子的高度

color = ['tab:red', 'y', 'tab:green']
for i in range(len(x)):
    for j in range(len(y)):
        ax.bar3d(x[i], y[j], 0, dx, dy, dz[j], shade=True, color=color[i], edgecolor='black',
                 linewidth=1, alpha=0.7)

# 创建虚拟的图例
rect1 = plt.Rectangle((0, 0), 1, 1, fc=color[0], edgecolor='black', linewidth=1)
rect2 = plt.Rectangle((0, 0), 1, 1, fc=color[1], edgecolor='black', linewidth=1)
rect3 = plt.Rectangle((0, 0), 1, 1, fc=color[2], edgecolor='black', linewidth=1)
ax.legend([rect1, rect2, rect3], ['Category 1', 'Category 2', 'Category 3'], loc='upper left')
# 添加横纵坐标label
ax.set_xlabel('X轴')
ax.set_ylabel('Y轴')
ax.set_zlabel('Z轴')

# 添加图的标题
plt.title('三维柱状图')

# 显示图形
plt.show()