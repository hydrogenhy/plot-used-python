"""
绘制柱状图(多组)代码。
在柱状图的基础上对每一组的若干指标进行整体绘制。
1.利于反映整体信息
2.兼具有柱状图的优势
"""
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换

# 生成示例数据
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
indicators = ['Indicator 1', 'Indicator 2', 'Indicator 3']
data = np.random.randint(1, 10, size=(5, 3))
print(data)

# 创建一个Figure对象和一个子图
fig, ax = plt.subplots()

# 设置每个柱子的宽度
width = 0.2

# 设置颜色列表
colors = ['b', 'g', 'r']

# 绘制柱状图
for i in range(len(groups)):
    x = (np.arange(len(indicators)) - len(indicators)//2) * width + i
    for j in range(len(indicators)):
        ax.bar(x[j], data[i][j], width, color=colors[j], label=indicators[j] if i == 0 else '')


# 添加图例
ax.legend(loc='upper right')

# 添加横纵坐标label
ax.set_xlabel('组', fontsize=12)
ax.set_ylabel('数值', fontsize=12)

# 设置图表标题
ax.set_title('柱状图(多组)', fontsize=14)

# 设置刻度标签
ax.set_xticks(np.arange(len(groups)))
ax.set_xticklabels(groups)

# 显示图形
plt.show()
