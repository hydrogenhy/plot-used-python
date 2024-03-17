"""
3D函数图像绘制代码
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换

# 定义函数
def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# 生成网格点
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
# print(X)
Z = f(X, Y)

# 创建3D图形对象
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# 绘制立体函数图像
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='black', alpha=0.8)

# 添加横纵坐标label
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 添加图的标题
plt.title('3D立体函数图像')

# 设置刻度标签
ax.set_xticks(np.arange(-5, 6, 2))
ax.set_yticks(np.arange(-5, 6, 2))
ax.set_zticks(np.arange(-1, 1.5, 0.5))

# 设置轴范围
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-1, 1)

# 添加颜色条
fig.colorbar(surf, shrink=0.5, aspect=5)

# 旋转视角，调整角度
ax.view_init(elev=30, azim=30)

# 隐藏边框
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('w')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')
ax.grid(True)

# 显示图形
plt.show()
