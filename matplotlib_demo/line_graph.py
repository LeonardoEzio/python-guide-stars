import numpy as np
import matplotlib.pyplot as plt


# 正弦函数图
def draw_sin_one():
    # 数据范围
    x_ranges = np.arange(0, 20)
    # 准备画布
    figure1 = plt.figure(figsize=(10, 10))
    # 绘制子图
    figure1.add_subplot(1, 1, 1)
    plt.title("y = sin(x)")
    plt.xlabel("X")
    plt.xlim([0, 20])
    plt.ylabel("Y")
    plt.ylim([-2, 2])
    plt.plot(x_ranges, np.sin(x_ranges))
    plt.show()


# 正弦函数图2
def draw_sin_two():
    # 数据范围 步长改为0.1
    x_ranges = np.arange(0, 20, 0.1)
    # 准备画布
    figure1 = plt.figure(figsize=(10, 10))
    # 绘制子图
    figure1.add_subplot(1, 1, 1)
    plt.title("y = sin(x)")
    plt.xlabel("X")
    plt.xlim([0, 20])
    plt.ylabel("Y")
    plt.ylim([-2, 2])
    plt.plot(x_ranges, np.sin(x_ranges))
    plt.show()


# 画个三角形
def draw_triangle():
    figure1 = plt.figure(figsize=(10, 10))
    figure1.add_subplot(1, 1, 1)
    plt.title("Draw Triangle")
    plt.xlabel("X")
    plt.xlim([0, 10])
    plt.ylabel("Y")
    plt.ylim([0, 10])
    plt.plot([0, 2, 5, 0], [0, 4, 7, 0])
    plt.show()


# 画个三角形
def draw_triangle_two():
    figure1 = plt.figure(figsize=(10, 10))
    figure1.add_subplot(1, 1, 1)
    plt.title("Draw Triangle")
    plt.xlabel("X")
    plt.xlim([0, 10])
    plt.ylabel("Y")
    plt.ylim([0, 10])
    # plt.plot([2, 10, 5, 2], [2, 2, 5, 2],  "o--r") 第三个参数为fmt, fmt语法如下
    # marker，也就是点的样式，这里的点指的就是数据源中传入的点；
    #
    # line，线的样式，比如有实线、虚线；
    #
    # color，也就是线条的颜色
    plt.plot([0, 2, 5, 0], [0, 4, 7, 0], "H-.r", markersize=10)
    plt.show()


def draw_point_graph():
    # 数据范围 步长改为0.1
    x_ranges = np.arange(0, 20, 0.5)
    # 准备画布
    figure1 = plt.figure(figsize=(10, 10))
    # 绘制子图
    figure1.add_subplot(1, 1, 1)
    plt.title("y = sin(x)")
    plt.xlabel("X")
    plt.xlim([0, 20])
    plt.ylabel("Y")
    plt.ylim([-2, 2])
    plt.scatter(x_ranges, np.sin(x_ranges), marker="*")
    plt.show()


if __name__ == "__main__":
    # draw_sin_one()
    draw_sin_two()
    # draw_triangle()
    # draw_triangle_two()
    # draw_point_graph()