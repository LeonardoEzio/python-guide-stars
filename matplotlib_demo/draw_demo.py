import numpy as np
import matplotlib.pyplot as plt


def test_draw():
    # 绘制 0 - 10 范围内的曲线
    # 定义数据源 0-10 范围
    x_ranges = np.arange(0, 10)

    # 创建画布
    # figure1 = plt.figure(figsize=(10, 10), facecolor=[0, 0, 0])
    figure1 = plt.figure(figsize=(10, 10))

    # 创建子图
    # add_subplot(行数，列数，当前子图索引)
    ax1 = figure1.add_subplot(1, 1, 1)

    # 设置子图标题 matplotlib内部维护了一个状态机，每次执行add_subplot的时候，会记录当前操作的子图，因此执行plt的方法时都是针对当前子图生效
    plt.title("y = 2x + 1")

    # 设置坐标轴的属性
    plt.xlabel("X")
    plt.xlim([0, 20])
    plt.ylabel("Y")
    plt.ylim([0, 20])

    # 绘制
    plt.plot(x_ranges, x_ranges * 2 + 1)
    plt.show()


# 多幅子图绘制
def test_draw_two():
    figure2 = plt.figure(figsize=[18, 9])
    # add_subplot 函数的形式如下：
    # add_subplot(行数，列数，当前子图索引)
    # 行数和列数代表子图的位置在画布中如何划分。比如如果是行数和列数都是 2 的话，代表把画纸拆分成 2x2，一共四个格子，
    # 每个格子可以放置一个子图。当前子图索引参数指的是告诉 Matplotlib 接下来要设置的是这个 2x2 的划分里的第几幅子图。
    ax1 = figure2.add_subplot(2, 2, 4)
    plt.title("draw one")

    ax2 = figure2.add_subplot(2, 2, 3)
    plt.title("draw two")

    ax3 = figure2.add_subplot(2, 2, 2)
    plt.title("draw three")

    ax4 = figure2.add_subplot(2, 2, 1)
    plt.title("draw four")

    plt.show()


if __name__ == "__main__":
    test_draw()
    test_draw_two()
