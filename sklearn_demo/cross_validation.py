from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score
import numpy as np
import matplotlib.pyplot as plt



iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)

k_range = range(1,31)
k_scores = []
for k in k_range:
	knn = KNeighborsClassifier(n_neighbors = k)
	loss = -cross_val_score(knn,X,y,cv=10,scoring='mean_squared_error')#for regression
#	scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')#for classification
	
	#knn.fit(X_train,y_train)
	#scores = knn.score(X_test,y_test)
	#scores = knn.score(X_train,y_train)

	#k_scores.append(scores.mean())
	k_scores.append(loss.mean())
	

plt.plot(k_range,k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Corss-Validated Accuracy')
plt.show()






















