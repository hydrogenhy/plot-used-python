"""
绘制桑基图的代码
"""
import plotly.graph_objects as go

# 输入数据
label = ["A", "B", "C", "D", "E"]
source = [0, 0, 1, 1, 2, 2, 3, 3]  # 前一列的索引
target = [2, 3, 2, 4, 3, 4, 3, 4]  # 后一列的索引
value = [8, 4, 2, 6, 2, 6, 4, 2]  # 对应的流量值

# 创建桑基图对象
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=label,
        # color="blue"  # 设置节点颜色
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
        # color="rgba(255, 0, 0, 0.5)",  # 设置链接颜色和透明度
    )
)])

# 设置图的标题和大小
fig.update_layout(title_text="桑基图", title_x=0.5, title_font_size=24)
fig.update_layout(width=800, height=600)

# 隐藏坐标轴
fig.update_xaxes(showline=False, showgrid=False, zeroline=False, showticklabels=False)
fig.update_yaxes(showline=False, showgrid=False, zeroline=False, showticklabels=False)

# 显示图形
fig.show()