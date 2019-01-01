from __future__ import print_function
from sklearn import datasets
from sklearn.linear_model import LinearRegression

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

model = LinearRegression()
#print('coef:',model.coef_) #is not timing error is weird
model.fit(data_X, data_y)

print(model.predict(data_X[:4,:]))
print(data_y[:4])

print('predict:',model.predict(data_X[:4,:]))
print('coef:',model.coef_)
print('intercept:',model.intercept_)
print('param:',model.get_params())
print(model.score(data_X, data_y))


############################################################










