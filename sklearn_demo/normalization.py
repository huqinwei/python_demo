from __future__ import print_function
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import preprocessing
from sklearn.datasets.samples_generator import make_classification
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

a = np.array([[10,2.7,3.6],[-100,5,-2],[120,20,40]],dtype=np.float64)
print(a)
print(preprocessing.scale(a))
print(preprocessing.minmax_scale(a,feature_range=(-2222,3333)))



X, y = make_classification(n_samples=300, n_features=2, n_redundant=0, n_informative=2,
			random_state=22, n_clusters_per_class=1, scale=100)
plt.scatter(X[:,0],X[:,1], c=y)
plt.show()

X = preprocessing.scale(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
clf = SVC()#new model
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))

#print('coef:',clf.coef_) #only in linear kernel




############################################################










