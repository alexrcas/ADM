import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from matplotlib import style
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor

boston = load_boston()


bostonpd = pd.DataFrame(boston.data)
bostonpd.columns = boston.feature_names
bostonpd["PRICE"] = boston.target
plt.scatter(bostonpd.RM, bostonpd.PRICE)
plt.xlabel('Número de habitaciones')
plt.ylabel('Precio')
plt.show()

#División del conjunto de datos
X = np.array(bostonpd.drop(['PRICE'], 1))
X = preprocessing.scale(X)
y = np.array(bostonpd['PRICE'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

#Regresión lineal
lr = LinearRegression()
lr.fit(X_train, y_train)
confidence = lr.score(X_test, y_test)
predict = lr.predict(X_test)
resta = np.mean(y_test - predict)

plt.scatter(y_test, predict)
plt.xlabel("Precios")
plt.ylabel("Precios Predecidos")
plt.show()



# Random forest
reg = RandomForestRegressor()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_train)
plt.scatter(y_train, y_pred)
plt.xlabel("Precios")
plt.ylabel("Precios predecidos")
plt.show()
