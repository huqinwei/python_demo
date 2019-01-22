import pickle

a = [1,2,[3,4]]
file = open('test.txt','w')
pickle.dump(a,file)
file.close()

file = open('test.txt','r')
b = pickle.load(file)
print(b)


