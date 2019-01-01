import os

#demo1
# path_ab = os.path.join('path_a','path_b')
# if os.path.exists(path_ab) is False:
#     os.makedirs(path_ab)

#demo2
path_abc = os.path.join('path_a2','path_b','path_c')

if os.path.exists(path_abc) is False:
    os.makedirs(path_abc)

#demo3
# path_abc = os.path.join('path_a2',['path_b','path_c'])#TypeError: join() argument must be str or bytes, not 'list'
#
# if os.path.exists(path_ab) is False:
#     os.makedirs(path_ab)



