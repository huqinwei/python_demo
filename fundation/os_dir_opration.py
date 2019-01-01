#file io demo
# mkdir  exists
import os

test_dir = 'exist_dir'
test_file = 'hello_foo.txt'

if not os.path.exists(test_dir):
  print(test_dir,' not exist!!!')
  os.makedirs(test_dir)
  #os.makedirs('exist_d', mode = , int = ,exist_ok = False)
else:
  print(test_dir,' is already exist!!!')
  if os.path.isfile(test_dir):
    print(test_dir,' is a file')
  if os.path.isdir(test_dir):
    print(test_dir,' is a directory')
  filepath = os.path.join(test_dir,test_file)
  if not os.path.exists(filepath):
    print(filepath,' not exist!!!')
  else:
    print(filepath,' exist!!!')
    fp = open(filepath,'r')
    print('read file:',fp.read())

  print('listdir:',os.listdir(test_dir))
  #print(os.listdir('../'))
  #print(os.listdir('./'))
  print('dirname:',os.path.dirname(test_dir))
  print('basename:',os.path.basename(test_dir))
  #os.mknod('test')
  fp = open(filepath, 'w')
  fp.write('hello file!')

