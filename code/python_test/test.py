import numpy as np
from sklearn import datasets, linear_model
from random import randint as ra
import matplotlib.pyplot as plt
# 定义训练数据
x = np.array([[ra(0,99)*0.01, ra(0,99)*0.01, ra(0,99)*0.01,ra(0,99)*0.01,ra(0,99)*0.01],
              [ra(0,99)*0.01, ra(0,99)*0.01, ra(0,99)*0.01,ra(0,99)*0.01,ra(0,99)*0.01],
              [ra(0,99)*0.01, ra(0,99)*0.01, ra(0,99)*0.01,ra(0,99)*0.01,ra(0,99)*0.01],
              [ra(0,99)*0.01, ra(0,99)*0.01, ra(0,99)*0.01,ra(0,99)*0.01,ra(0,99)*0.01],
              [ra(0,99)*0.01, ra(0,99)*0.01, ra(0,99)*0.01,ra(0,99)*0.01,ra(0,99)*0.01],
              [ra(0,99)*0.01, ra(0,99)*0.01, ra(0,99)*0.01,ra(0,99)*0.01,ra(0,99)*0.01],
              [ra(0,99)*0.01, ra(0,99)*0.01, ra(0,99)*0.01,ra(0,99)*0.01,ra(0,99)*0.01],
              [ra(0,99)*0.01, ra(0,99)*0.01, ra(0,99)*0.01,ra(0,99)*0.01,ra(0,99)*0.01],
              [ra(0,99)*0.01, ra(0,99)*0.01, ra(0,99)*0.01,ra(0,99)*0.01,ra(0,99)*0.01],
              [ra(0,99)*0.01, ra(0,99)*0.01, ra(0,99)*0.01,ra(0,99)*0.01,ra(0,99)*0.01]])
X = x[:, :-1]
Y = x[:, -1]

# 训练数据
regr1 = linear_model.Lasso(normalize=True, alpha=0.01,warm_start=True,fit_intercept=True)  # L1正则
regr1.fit(X, Y)
# 预测
x_test1 = np.array([[ra(0,99)*0.01, ra(0,99)*0.01,ra(0,99)*0.01,ra(0,99)*0.01]])

# 训练数据
regr2 = linear_model.LinearRegression()          # 多元线性回归
regr2.fit(X, Y)
# 预测
y_test2 = regr2.predict(x_test1)#糖度
print("糖度:")
print(y_test2)