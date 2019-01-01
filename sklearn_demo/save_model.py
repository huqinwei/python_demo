from sklearn import svm
from sklearn import datasets

classifier = svm.SVC()
iris = datasets.load_iris()
X,y = iris.data,iris.target

classifier.fit(X,y)

import pickle
#with open('save/clf.pickle','wb') as f:
#	pickle.dump(classifier,f)

#with open('save/clf.pickle','rb') as f:
#	classifier2 = pickle.load(f)
#print(classifier2.predict(X[0:]))
#print(y[0:])


from sklearn.externals import joblib
#joblib.dump(classifier,'save/clf.pkl')

classifier3 = joblib.load('save/clf.pkl')
print(classifier3.predict(X[:]))
print(y[:])
print(type(classifier3))







