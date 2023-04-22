import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
import sklearn.metrics as mt
import seaborn as sns

data=pd.read_csv('/home/barbaros/Desktop/Aı/6_Basit_Lineer_Regresyon/data/Advertising.csv', index_col=0)
X=data['TV']
y=data['sales']
X=X.values.reshape(-1,1)
y=y.values.reshape(-1,1)
"""print(X.shape)
plt.figure(figsize=(12, 8))
sns.scatterplot(data=data, x='TV', y='sales', color='red')
plt.title("Sales-TV")
plt.show()"""
lr=LinearRegression()
r2_l=[]
lis=[]
for i in range (100):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=i)
    lr.fit(X_train, y_train)
    y_pred=lr.predict(X_test)
    a=mt.r2_score(y_test,y_pred)
    k=(i,a)
    lis.append(k)

print(lis)
en_kucuk = lis[0][1]
en_buyuk = lis[0][1]
for n in lis:
  x=n
  n=n[1]
  if en_buyuk > n:
    en_buyuk=n
    b=x
  if en_kucuk <n:
    en_kucuk=n
    k=x
print(b)
print(k)