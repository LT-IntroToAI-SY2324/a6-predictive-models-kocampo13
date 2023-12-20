# Project - Create your own predictive model
# Cat Markowska and Kelly Ocampo, P.3

from ucimlrepo import fetch_ucirepo 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo 
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# fetch dataset 
abalone = fetch_ucirepo(id=1) 
  
# data
x = abalone.data.features 
y = abalone.data.targets 
  
# metadata 
print(abalone.metadata) 
  
# variable information 
print(abalone.variables) 

data = pd.read_csv("final-project/abalone_data.csv")
data = data[["height", "length"]]

x_std = StandardScaler().fit_transform(data)

k = 5
km = KMeans(n_clusters=k).fit(x_std)

centroids = km.cluster_centers_
labels = km.labels_

plt.figure(figsize=(5,4))

for i  in range(k):
    cluster = x[labels == i]
    plt.scatter(cluster[:, 0], cluster[:, 1])

plt.scatter(centroids[:, 0], centroids[:, 1], marker = 'x', s = 100,
c = 'r', label = 'centroid')

plt.xlabel("Height of Abalone")
plt.ylabel("Length of Abalone")
plt.show()
