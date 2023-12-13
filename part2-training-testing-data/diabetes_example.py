import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, linear_model 
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# load dataset

x, y = datasets.load_diabetes(return_X_y=True)
x = x[:,np.newaxis, 2]


xtrain, xtest, ytrain, ytest = train_test_split(x, y, test)




model = linear_model.LinearRegression