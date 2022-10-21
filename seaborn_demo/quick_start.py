import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


# 直方图绘制
def random_drawn():
    np.random.seed(100)
    hints = np.random.normal(5, 10, 1000)
    figure1 = plt.figure(figsize=(10, 5))
    figure1.add_subplot(1, 1, 1)
    plt.hist(hints, bins=50)
    plt.show()


def random_drawn_with_seaborn_style():
    sns.set()
    np.random.seed(100)
    hints = np.random.normal(5, 10, 1000)
    figure1 = plt.figure(figsize=(10, 5))
    figure1.add_subplot(1, 1, 1)
    plt.hist(hints, bins=50)
    plt.show()


def get_analysis_data():
    df_iris = px.data.iris()
    return df_iris


def quick_drawn():
    data = get_analysis_data()
    data.petal_width.plot()
    plt.show()


def quick_drawn_all_filed():
    data = get_analysis_data()
    data.plot()
    plt.show()


# 直方图
def histogram_drawn():
    sns.set()
    data = get_analysis_data()
    data.petal_width.plot.hist()
    plt.show()


# kdeplot 核密度图
def kdeplot_demo():
    data = get_analysis_data()
    sns.kdeplot(data.petal_width, shade=True)
    plt.show()


# 直方核密度图
def histogram_and_kdeplot_drawn():
    data = get_analysis_data()
    sns.histplot(data.petal_width, kde=True)
    plt.show()


def two_dimensional_kernel_density_map():
    sns.kdeplot(data=get_analysis_data(), x="petal_width", y="sepal_width", shade=True)
    plt.show()


# 相关性图表
def pair_plot():
    data = get_analysis_data()
    real_data = data.drop(columns=["species_id"])
    sns.pairplot(real_data)
    plt.show()


if __name__ == "__main__":
    # random_drawn_with_seaborn_style()
    # quick_drawn()
    # quick_drawn_all_filed()
    # kdeplot_demo()
    # histogram_drawn()
    # histogram_and_kdeplot_drawn()
    # two_dimensional_kernel_density_map()
    pair_plot()