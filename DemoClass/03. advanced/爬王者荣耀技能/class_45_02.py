# 学习朴素贝叶斯方法
import numpy as np
from sklearn.datasets import load_iris

# 加载鸢尾花数据集

data = load_iris()
data = data.data       # 取出数据集

print(data)


