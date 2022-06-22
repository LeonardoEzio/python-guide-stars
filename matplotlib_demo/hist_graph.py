import numpy as np
import matplotlib.pyplot as plt


# 随机分布直方图
def draw_random_hist():
    np.random.seed(100)
    hints = np.random.normal(5, 10, 1000)
    print(hints.mean(), hints.std())
    # 创建画布
    figure = plt.figure(figsize=(10, 5))
    figure.add_subplot(1, 1, 1)
    plt.xlabel("值", fontsize=14)
    plt.ylabel("频率", fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.title("正态分布的直方图", fontsize=14)
    plt.rcParams["font.sans-serif"] = "SimHei"
    plt.rcParams["axes.unicode_minus"] = False
    # bins 参数决定了数据分多少组 同时可以通过 edgecolor参数给边框加颜色
    plt.hist(hints, bins=50, color=[0, 0, 1], edgecolor=[0, 0, 0])
    plt.show()


if __name__ == "__main__":
    draw_random_hist()
