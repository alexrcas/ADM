import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from urllib.request import urlopen

from pandas import DataFrame




with urlopen('https://raw.githubusercontent.com/datadista/datasets/master/COVID%2019/nacional_covid19_rango_edad.csv') as response:
    df = pd.read_csv(response)




fallecidos_grouped = df.groupby('rango_edad').sum()

# X = np.array(fallecidos_grouped['rango_edad'])
# Y = np.array(fallecidos_grouped['fallecidos'])

print(fallecidos_grouped)

# songs_grouped['success'] = songs_grouped['position'] < 15
# songs_grouped['success'] = songs_grouped['success'].astype(int)

rango_edad = DataFrame(df['rango_edad'].unique(), columns=['rango_edad']) 
print(rango_edad)
X = np.array(rango_edad, fallecidos_grouped['casos_confirmados'])
Y = np.array(fallecidos_grouped['fallecidos'])



# kmeans = KMeans(n_clusters = 4 ).fit(X)
# centroids = kmeans.cluster_centers_
# labels = kmeans.predict(Y)

# colors = ['blue', 'red', 'green']
# assign = []
# for row in labels:
#     assign.append(colors[row])


# f1 = df['rango_edad'].unique()
# print(f1)
# f2 = fallecidos_grouped['fallecidos']

# plt.scatter(f1, f2, s=70)
# plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', c=colors, s=500)
# plt.show()