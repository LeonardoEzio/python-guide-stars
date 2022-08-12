import matplotlib.pyplot as plt


# 单个饼图绘制
def draw_single_pie():
    fig = plt.figure(figsize=(10, 5))
    fig.add_subplot(1, 1, 1)
    plt.rcParams["font.sans-serif"] = "SimHei"
    plt.rcParams["axes.unicode_minus"] = False
    # 设置饼图数据源
    category = ["没有得过", "得过一次", "得过两次", "得过三次以上"]
    size = [40, 30, 25, 5]
    # 绘图颜色
    color = ["r", "g", "b", "c"]
    explode = [0, 0, 0, 0.1]
    # 绘制饼图
    plt.pie(size, explode=explode, colors=color, labels=category, labeldistance=1.1, autopct="%1.1f%%", startangle=90, pctdistance=0.6)
    plt.show()


def draw_multi_pie():
    week_category = ["第一周", "第二周", "第三周", "第四周"]
    sales_a = [10, 23, 5, 11]
    sales_b = [3, 12, 6, 5]
    # 创建画布
    fig = plt.figure(figsize=(10, 10))
    plt.rcParams["font.sans-serif"] = "SimHei"
    plt.rcParams["axes.unicode_minus"] = False
    for i in range(0, 4):
        fig.add_subplot(2, 2, i+1)
        plt.title(week_category[i])
        category = ["销售A", "销售B"]
        size = [sales_a[i], sales_b[i]]
        color = ["b", "g"]
        explode = [0, 0]
        plt.pie(size, explode=explode, colors=color, labels=category, labeldistance=1.1, autopct="%1.1f%%", startangle=90, pctdistance=0.6)
    plt.show()


if __name__ == "__main__":
    # draw_single_pie()
    draw_multi_pie()
