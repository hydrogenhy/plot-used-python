"""
绘制柱状图的代码。
1.易于理解：柱状图是一种直观的图表类型，可以清晰地展示数据之间的差异和相对大小。每个柱子的高度表示数据的数量或值，使观众能够快速理解数据的特征。
2.比较数据：柱状图特别适用于比较多组数据之间的差异。通过将不同类别的数据放置在同一张图表上，柱状图可以直观地呈现它们之间的关系，帮助观众发现数据的模式和趋势。
3.可视化分布：柱状图可以用于展示数据的分布情况。例如，可以使用柱状图来显示数据的频率分布或类别分布。
4.强调异常值：柱状图能够很容易地识别出数据的异常值。高于或低于其他柱子的柱状图很可能是异常值，使我们能够快速定位数据中的异常情况。
5.可用于大数据集：柱状图适用于大量数据的可视化，特别是类别较多的情况。不同类别的柱状图可以并排显示，不会造成混乱。
6.易于与其他图表结合：柱状图可以很容易地与其他图表结合使用，如折线图、堆积柱状图等。这样，可以更全面地展示数据的不同方面。
"""
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换

# 数据示例，假设有五个数据的高度
heights = [5, 7, 3, 4, 6]
x = [i for i in range(len(heights))]

# 创建一个Figure对象和一个子图
fig, ax = plt.subplots()

# 不同柱子的填充样式和颜色
# patterns = ['/', 'x', '+', '-', 'o']
patterns = ['', '', '', '', '']
colors = ['blue', 'green', 'red', 'purple', 'orange']
# 绘制柱状图
width = 0.5  # 柱状图宽度

for i in range(len(heights)):
    bar = ax.bar(x[i], heights[i], width, color=colors[i], hatch=patterns[i], label=f'Bar {i+1}')  # 绘制
    height = bar[0].get_height()
    ax.annotate(f'{height}', xy=(bar[0].get_x() + bar[0].get_width() / 2, height), xytext=(0, 3),
                textcoords="offset points", ha='center', va='bottom')  # 在柱状图上添加对应数据

# 添加图例
ax.legend(fontsize=12, loc='best')

# 添加横纵坐标label
ax.set_xlabel('X轴', fontsize=14, fontweight='bold')
ax.set_ylabel('Y轴', fontsize=14, fontweight='bold')

# 设置xy范围
plt.ylim([0, 10])

# 设置图表标题
ax.set_title('柱状图', fontsize=16, fontweight='bold')

# 设置刻度标签
ax.set_xticks(x)
ax.set_xticklabels([f'Bar {i+1}' for i in range(len(heights))], fontsize=12, fontweight='bold')

# 设置网格线
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 设置背景颜色
ax.set_facecolor('#f0f0f0')

# 去除图表边框
for spine in ax.spines.values():
    spine.set_visible(False)

# 显示图形
plt.show()
