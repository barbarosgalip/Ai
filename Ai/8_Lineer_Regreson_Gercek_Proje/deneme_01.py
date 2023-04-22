import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from sklearn.feature_selection import RFE
warnings.simplefilter(action='ignore', category=Warning)

df = pd.read_csv("/home/barbaros/Desktop/Aı/8_Lineer_Regreson_Gercek_Proje/data/Automobile.csv", index_col=1)
print(df.carname)

