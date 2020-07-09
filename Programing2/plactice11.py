import numpy as np
from sklearn.cluster import KMeans
features = np.random.randint(45, 100, (100,3))

seed = 1
model = KMeans(n_clusters=3, random_state=seed).fit(features)

labels = model.labels
for label, feature in zip(labels, features):
    print(label, feature)

