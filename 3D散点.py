"""
3D散点图像绘制代码
"""
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换

# 生成示例数据
np.random.seed(0)
cluster1 = np.random.randn(100, 3) + [3, 3, 3]
cluster2 = np.random.randn(100, 3) + [-2, -2, -2]
cluster3 = np.random.randn(100, 3) + [1, -1, 4]

# 创建3D图形对象
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制三维数据点
ax.scatter(cluster1[:, 0], cluster1[:, 1], cluster1[:, 2], color='r', marker='o', label='Cluster 1', alpha=0.8)
ax.scatter(cluster2[:, 0], cluster2[:, 1], cluster2[:, 2], c='g', marker='^', label='Cluster 2', alpha=0.8)
ax.scatter(cluster3[:, 0], cluster3[:, 1], cluster3[:, 2], c='b', marker='s', label='Cluster 3', alpha=0.8)

# 添加图例，设置位置为右上角
ax.legend(loc='upper right')

# 添加横纵坐标label
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 添加图的标题
plt.title('三维三点聚类图像', fontsize=16, fontweight='bold')

# 设置坐标轴刻度范围
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_zlim(-6, 6)

# 设置坐标轴刻度间隔
# ax.set_xticks(np.arange(-6, 7, 2))
# ax.set_yticks(np.arange(-6, 7, 2))
# ax.set_zticks(np.arange(-6, 7, 2))


# 隐藏边框和网格
# ax.xaxis.pane.fill = False
# ax.yaxis.pane.fill = False
# ax.zaxis.pane.fill = False
# ax.xaxis.pane.set_edgecolor('black')
# ax.yaxis.pane.set_edgecolor('black')
# ax.zaxis.pane.set_edgecolor('black')
# ax.grid(True)


# 调整视角
ax.view_init(elev=20, azim=30)

# 显示图形
plt.show()