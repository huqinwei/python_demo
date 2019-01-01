#大意就是，既然是脚本，引入了肯定会执行，用name来控制外来模块不执行
print('using_name.py running or importing!!!')
if __name__ == '__main__':
    print('this is in using_name.py')
else:
    print('this is a module imported')
