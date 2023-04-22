import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
df = pd.read_csv('/home/barbaros/Desktop/3_Giris_Kavramlari_ve_Notasyon/1_Giris_Kavramlari/NCI60.csv')
pca= PCA(n_components=2)
X = df.iloc[:, 1:6831]
scale = StandardScaler()

X_scaled = scale.fit_transform(X)
pca_result=pca.fit_transform(X_scaled)

