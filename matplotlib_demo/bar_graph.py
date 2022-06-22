import numpy as np
import matplotlib.pyplot as plt


# 图像会根据绘制次序堆叠
def draw_random_bar():
    math_scores = np.array([71, 65, 70, 96, 64])
    chinese_scores = np.array([84, 75, 68, 83, 57])
    english_scores = np.array([55, 78, 76, 91, 64])
    # 创建画布
    figure = plt.figure(figsize=(10, 5))
    figure.add_subplot(1, 1, 1)
    # 设置轴属性
    plt.xlabel("", fontsize=14)
    plt.ylabel("平均分", fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.title("期中成绩条形图", fontsize=14)
    #  设置画布基本属性：1.显示中文  2.显示负号
    plt.rcParams["font.sans-serif"] = "SimHei"
    plt.rcParams["axes.unicode_minus"] = False
    category = ["一班", "二班", "三班", "四班", "五班"]

    #  语文成绩用蓝色
    plt.bar(category, chinese_scores, color=[0, 0, 1])
    #  数学成绩，用绿色
    plt.bar(category, math_scores, color=[0, 1, 0])
    #  英语成绩，用红色
    plt.bar(category, english_scores, color=[1, 0, 0])
    plt.show()


# 不同颜色分组条形图
def draw_random_bar_two():
    math_scores = np.array([71, 65, 70, 96, 64])
    chinese_scores = np.array([84, 75, 68, 83, 57])
    english_scores = np.array([55, 78, 76, 91, 64])
    # 创建画布
    figure = plt.figure(figsize=(10, 5))
    figure.add_subplot(1, 1, 1)
    # 设置轴属性
    plt.xlabel("", fontsize=14)
    plt.ylabel("平均分", fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.title("期中成绩条形图", fontsize=14)
    #  设置画布基本属性：1.显示中文  2.显示负号
    plt.rcParams["font.sans-serif"] = "SimHei"
    plt.rcParams["axes.unicode_minus"] = False
    category = ["一班", "二班", "三班", "四班", "五班"]
    index_category = np.arange(len(category))
    bar_width = 0.25
    #  语文成绩用蓝色
    plt.bar(index_category-bar_width, chinese_scores, width=bar_width, color=[0, 0, 1])
    #  数学成绩，用绿色
    plt.bar(index_category, math_scores, width=bar_width, color=[0, 1, 0])
    #  英语成绩，用红色
    plt.bar(index_category+bar_width, english_scores, width=bar_width, color=[1, 0, 0])
    plt.show()


# 堆叠条形图绘制
def draw_random_bar_three():
    figure4 = plt.figure(figsize=(10, 5))
    figure4.add_subplot(1, 1, 1)
    plt.xlabel("", fontsize=14)
    plt.ylabel("签单量", fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.title("签单堆叠条形图", fontsize=14)
    plt.rcParams["font.sans-serif"] = "SimHei"
    plt.rcParams["axes.unicode_minus"] = False
    #  横轴数据
    category = ["第一周", "第二周", "第三周", "第四周"]
    #  两个销售各周的销量
    sales_a = [10, 23, 5, 11]
    sales_b = [3, 12, 6, 5]
    #  首先画销售A, 用紫色
    plt.bar(category, sales_a, color=[1, 0, 1])
    #  然后用蓝色画销售B，并指定 bottom为销售a的数据
    plt.bar(category, sales_b, color=[0, 0, 1], bottom=sales_a)
    plt.show()


if __name__ == "__main__":
    # draw_random_bar()
    # draw_random_bar_two()
    draw_random_bar_three()
