import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
df = pd.read_csv('/home/barbaros/Desktop/3_Giris_Kavramlari_ve_Notasyon/1_Giris_Kavramlari/NCI60.csv')
x=df.iloc[:, 1:6831]
sc=StandardScaler()
pca=PCA(n_components=3)
x_sc=sc.fit_transform(x)
pcar=pca.fit_transform(x_sc)

data= pd.DataFrame(data=pcar, columns=['1','2','3'])
final=pd.concat([data, df[['labs']]], axis=1)
print(final)