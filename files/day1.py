#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/8/9 12:17 上午
# @Author : Jamerri
# @FileName: day1.py
# @Email : jamerri@163.com
# @Software: PyCharm

import numpy as np
import pandas as pd

dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

from sklearn.preprocessing import Impute
imputer = Impute(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[ : , 1:3] = imputer.transform(X[ : , 1:3])
