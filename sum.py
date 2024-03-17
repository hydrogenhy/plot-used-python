import matplotlib.pyplot as plt

def plot_bar(heights):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    x = [i for i in range(len(heights))]

    fig, ax = plt.subplots()

    patterns = ['', '', '', '', '']
    colors = ['blue', 'green', 'red', 'purple', 'orange']
    width = 0.5

    for i in range(len(heights)):
        bar = ax.bar(x[i], heights[i], width, color=colors[i], hatch=patterns[i], label=f'Bar {i+1}')
        height = bar[0].get_height()
        ax.annotate(f'{height}', xy=(bar[0].get_x() + bar[0].get_width() / 2, height), xytext=(0, 3),
                    textcoords="offset points", ha='center', va='bottom')

    ax.legend(fontsize=12, loc='best')
    ax.set_xlabel('X轴', fontsize=14, fontweight='bold')
    ax.set_ylabel('Y轴', fontsize=14, fontweight='bold')
    plt.ylim([0, max(heights) + 2])
    ax.set_title('柱状图', fontsize=16, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([f'Bar {i+1}' for i in range(len(heights))], fontsize=12, fontweight='bold')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_facecolor('#f0f0f0')
    for spine in ax.spines.values():
        spine.set_visible(False)
    plt.show()


