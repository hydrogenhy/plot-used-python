"""
绘制饼图的代码。
1.显示比例关系：饼图能够直观地显示数据各部分与整体的比例关系，帮助人们快速了解数据的分布情况。
2.突出占比较大部分：饼图的饼片大小与所占比例成正比，使得占比较大的部分更加突出，便于观察主要数据。
3.相对数量比较：饼图适用于展示相对数量的比较，特别是对于几个类别之间的比例关系。
4.简单易懂：饼图是一种简单易懂的图表类型，不需要复杂的数学知识就可以理解数据的占比情况。
5.适用于少量分类：饼图适用于较少的分类，当分类较多时，饼图的可读性和解析性可能会下降。
6.可以显示百分比：饼图可以自动计算并显示每个类别的百分比，进一步增强了数据的可读性。
7.适用于非连续数据：饼图适用于离散的、非连续的数据，如分类数据、百分比等。
"""
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换

# 生成示例数据
labels1 = ['Group 1', 'Group 2', 'Group 3']
labels2 = ['Group 4', 'Group 5', 'Group 6']
sizes1 = [30, 20, 50]
sizes2 = [25, 35, 30]  # 这里存放数据，并不是比例，因此求和不一定是100

# 设置颜色列表
colors1 = ['tab:blue', 'tab:orange', 'tab:green']
colors2 = ['tab:red', 'tab:purple', 'tab:brown']

# 创建一个Figure对象和一个子图
fig, ax = plt.subplots()

# 绘制饼图，并设置样式和颜色
wedges1, texts1, autotexts1 = ax.pie(sizes1, pctdistance=0.8, labels=labels1, colors=colors1, autopct='%1.2f%%',
                                     startangle=90, wedgeprops=dict(edgecolor='w'))  # pctdistance=0.8调整文字位置
wedges2, texts2, autotexts2 = ax.pie(sizes2, colors=colors2, radius=0.5, autopct='%1.1f%%', startangle=90,
                                     wedgeprops=dict(edgecolor='w'))  # radius=0.5调整半径大小

# 设置文本标签字体大小和颜色
for autotext in autotexts1 + autotexts2:
    autotext.set_fontsize(15)
    # autotext.set_color('white')

# 设置图例
ax.legend(wedges1 + wedges2, labels1 + labels2, loc='best')

# 添加图表标题
ax.set_title('三组数据的饼图', fontsize=14, fontweight='bold')

# 设置背景颜色
ax.set_facecolor('#f0f0f0')

# 显示图形
plt.show()
