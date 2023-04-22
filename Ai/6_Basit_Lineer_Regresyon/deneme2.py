import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as lr
from sklearn.ensemble import RandomForestClassifier 
import sklearn.metrics as mt



dataset=pd.read_csv('data/sayılar.csv')
x=dataset.iloc[:, 0].values.reshape(-1,1)
y=dataset.iloc[:, 1].values.reshape(-1,1)
rf=RandomForestClassifier(random_state=20, n_estimators=10)

rf.fit(x,y)

y_pred=rf.predict(x)


print(mt.r2_score(y, y_pred))
plt.plot(x, y_pred, color='b', label="poly" )
plt.legend()
plt.scatter(x,y, color='red')
plt.show()