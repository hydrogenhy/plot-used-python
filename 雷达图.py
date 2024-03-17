"""
绘制雷达图的代码。
可以用来对“属性”进行刻画
1.多变量比较：雷达图在展示多个变量之间的关系和差异方面具有优势，可以直观地展示数据在不同维度上的表现。
2.易于解读：雷达图是一种直观的图表类型，无需深入的数学知识即可理解数据的多维特征，使得数据分析和传达更容易。
3.数据关联性：雷达图将多个变量的信息集中在一个图形中展示，有助于观察不同维度之间的关联性，帮助我们发现隐藏在数据背后的规律。
4.强调相对比较：雷达图更注重相对的大小和差异，而非绝对数值，适用于比较多组数据在各个维度上的表现。
5.高效传递信息：雷达图以图形化的方式呈现多维数据，使得大量信息能够被快速有效地传达给观众。
"""
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换


# 示例数据：每个维度的数据值（三组数据）
categories = ['A', 'B', 'C', 'D', 'E']  # 维度名称
values1 = [4, 2, 3, 5, 4, 1]  # 第一组数据值
values2 = [3, 4, 2, 6, 3, 2]  # 第二组数据值
values3 = [2, 3, 5, 4, 5, 3]  # 第三组数据值

# 将第一个维度值复制到最后，以形成闭合
values1 += values1[:1]
values2 += values2[:1]
values3 += values3[:1]

# 计算每个维度对应的角度
angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)

# 将角度与数据值对应起来
angles = np.concatenate((angles, [angles[0]]))

# 创建一个Figure对象和一个子图，使用极坐标
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# 绘制三组雷达图，并设置样式
ax.plot(angles, values1, linewidth=1.5, linestyle='--', color='b', label='数据1')
ax.fill(angles, values1, alpha=0.3, color='b')

ax.plot(angles, values2, linewidth=1.5, linestyle='-.', color='g', label='数据2')
ax.fill(angles, values2, alpha=0.3, color='g')

ax.plot(angles, values3, linewidth=1.5, linestyle='solid', color='r', label='数据3')
ax.fill(angles, values3, alpha=0.3, color='r')

# 添加图例
ax.legend(loc='upper right', fontsize=12)

# 设置雷达图的标题
ax.set_title('雷达图', fontsize=16, fontweight='bold')

# 设置角度刻度，即设置维度的标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

# 设置刻度标签字体大小
ax.tick_params(axis='both', labelsize=12)

# 设置背景颜色
ax.set_facecolor('#f0f0f0')

# 设置图表边框颜色
ax.spines['polar'].set_color('#b0b0b0')

# 隐藏雷达图的刻度线
# ax.xaxis.grid(False)

# 显示图形
plt.tight_layout()
plt.show()