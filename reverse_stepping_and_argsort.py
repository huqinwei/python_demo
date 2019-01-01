import numpy as np
x = np.array([3, 0, 7, -1, 9, 5])
i = x.argsort()

print('stepping:',x[::1])
print('reverse stepping:',x[::-1])


for index_ in i:
    print(x[index_])

print(x)
print('i:',i)
print('-i:',-i)

print('x[i]):',x[i])
print('x[-i]):',x[-i])#cannot range reversely!!!!!!!!!!!!!!!!!


# top_k = predictions.argsort()[-FLAGS.num_top_predictions:][::-1]
print(x[-5:])
print('index:', x.argsort()[-5:])
print('index:', x.argsort()[-6:])
print('wrong demo:', x.argsort()[x.argsort()[-6:]])#nonsense
print(x[x.argsort()[-7:]])#upsent order of x

#print(i[-6:])

index_list = x.argsort()[-7:]#upsent order of x
for i_ in index_list:
    print('x:', x[i_])

index_list = x.argsort()[-7:][::-1]  # descent order of x
for i_ in index_list:
    print('x:', x[i_])