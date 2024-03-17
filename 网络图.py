"""
绘制网络图的代码。
能够对图结构进行直观刻画，可用于路径规划等问题。
同样树结构也能够用这个代码来画，因为树是特殊的有向无环图
这个网站也可以：https://csacademy.com/app/graph_editor/
1.多对多关系：网络图能够展示多个节点之间的多对多关系，适用于描述复杂的关联和连接。
2.可视化复杂结构：网络图可以清晰地展示节点之间的连接和关系，便于理解和观察复杂结构。
3.节点和边属性：网络图的节点和边可以附带属性信息，使得数据可以更加丰富，节点和边的样式和颜色可以代表不同的属性。
4.异构性：网络图可以描述异构性的数据，即不同类型的节点和边可以同时存在，能够展示多种类型的关系。
5.图算法应用：网络图的特点使得其在图算法（例如路径查找、社区发现等）方面具有广泛的应用。
6.强调连接：网络图强调节点之间的连接关系，使得观察和分析节点的交互和连接变得更加直观。
"""
import matplotlib.pyplot as plt
import networkx as nx
plt.rcParams['font.sans-serif'] = ['SimHei']  # 为了支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 上述字库没负号，因此负号不进行字体变换

# 创建一个简单的网络图
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
G.add_edges_from([('A', 'B'), ('B', 'C'), ('A', 'C'), ('C', 'E'), ('C', 'F'), ('B', 'D'), ('D', 'F'), ('G', 'F'), ('E', 'G')])

# 绘制网络图
pos = nx.circular_layout(G)  # 设置节点的位置

# 调整节点和边的样式
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1000, label='节点')
nx.draw_networkx_edges(G, pos, edge_color='gray', width=2)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# 添加图例
plt.legend()

# 添加图的标题
plt.title('网络图', fontsize=16, fontweight='bold')

# 设置背景颜色
plt.gca().set_facecolor('#f0f0f0')

# 隐藏坐标轴
plt.axis('off')

# 调整图例的位置
plt.legend(loc='upper right')

# 显示图形
plt.show()
