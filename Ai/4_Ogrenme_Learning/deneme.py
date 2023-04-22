import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df=pd.read_csv('/home/barbaros/Desktop/Aı/4_Ogrenme_Learning/data/Advertising.csv', index_col=0)

x1=df['TV']
x2=df['radio']
x3=df['newspaper']
y=df['sales']
print(x1)
lr=LinearRegression()
y_r=y.values.reshape(-1,1)
x1_r=x1.values.reshape(-1,1)
x2_r=x2.values.reshape(-1,1)
x3_r=x3.values.reshape(-1,1)

plt.scatter(x1_r, y_r, c='orange')
plt.scatter(x1, y, c='blue')
plt.show()