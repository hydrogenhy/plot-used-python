"""
绘制散点图代码。
经常用于对聚类结果的可视化。
1.显示数据分布：散点图能够清晰地展示数据点在二维坐标系中的分布情况，帮助我们了解数据的密度和分布规律。
2.可视化关系：散点图可以直观地显示两个变量之间的关系。通过观察散点图的分布模式，我们可以判断两个变量之间是否存在线性或非线性关系。
3.发现异常值：散点图可以帮助我们快速识别数据中的异常值。异常值通常是与其他数据点明显偏离的点，容易在散点图中显现出来。
4.可用于大数据集：散点图适用于大量数据的可视化。虽然对于大数据集，点可能会重叠，但散点图仍然能够展示数据点的总体分布和趋势。
5.可用于多变量比较：散点图可以同时显示多个变量之间的关系。通过使用不同颜色或标记样式，可以将多个数据集或组别在同一张散点图上比较，帮助发现模式和差异。
5.易于解读：散点图是一种简单而直观的图表类型，不需要复杂的数学知识就可以理解数据之间的关系和趋势。
6.用于数据预处理：在数据分析的早期阶段，散点图常常用于对数据进行初步探索和预处理，帮助我们了解数据的特点和潜在问题。
"""
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换

# 生成示例数据
np.random.seed(0)
data = np.random.rand(100, 2) * 5  # 100个随机数据点，取值范围在[0, 5)

# 使用K-Means算法进行聚类
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
labels = kmeans.fit_predict(data)

# 创建一个Figure对象和一个子图
fig, ax = plt.subplots()

# 设置颜色列表和标记样式列表
colors = ['tab:blue', 'tab:orange', 'tab:green']
markers = ['o', 's', 'D']

# 绘制散点图，并根据聚类结果使用不同的颜色和标记样式
for i in range(num_clusters):
    cluster_data = data[labels == i]
    ax.scatter(cluster_data[:, 0], cluster_data[:, 1], marker=markers[i], color=colors[i], label=f'Cluster {i+1}')

# 添加图例
ax.legend()

# 添加横纵坐标label
ax.set_xlabel('X轴', fontsize=12, fontweight='bold')
ax.set_ylabel('Y轴', fontsize=12, fontweight='bold')

# 设置图表标题
ax.set_title('聚类结果散点图', fontsize=14, fontweight='bold')

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

'''
# 单纯进行散点图绘制：
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体

# 生成示例数据
x = np.random.rand(50)
y1 = np.random.rand(50)
y2 = np.random.rand(50)
y3 = np.random.rand(50)
y4 = np.random.rand(50)
y5 = np.random.rand(50)

# 创建一个Figure对象和一个子图
fig, ax = plt.subplots()

# 绘制散点图
ax.scatter(x, y1, marker='o', color='b', label='Group 1')
ax.scatter(x, y2, marker='x', color='g', label='Group 2')
ax.scatter(x, y3, marker='+', color='r', label='Group 3')
ax.scatter(x, y4, marker='*', color='c', label='Group 4')
ax.scatter(x, y5, marker='s', color='m', label='Group 5')

# 添加图例
ax.legend()

# 添加横纵坐标label
ax.set_xlabel('X轴', fontsize=12)
ax.set_ylabel('Y轴', fontsize=12)

# 设置图表标题
ax.set_title('五组数据的散点图', fontsize=14)

# 显示图形
plt.show()
'''