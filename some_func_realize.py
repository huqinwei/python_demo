# Python3 实例


# Python 数字求和
# num1 = input('input number1:')
# num2 = input('input number2:')
#
# sum = float(num1) + float(num2)
#
# print('sum is ',sum)



#Python 平方根
# import cmath
#
# num = float(input('input a number:'))
# num2 = int(input('input a number:'))
# num_sqrt = num ** 0.5
# num_sqrt2 = cmath.sqrt(num2)
# print('%0.3f\'s  squart is %0.3f'%(num,num_sqrt))
# print('%0.3f\'s  squart is %0.3f'%(num2,num_sqrt2.real))
# print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num2 ,num_sqrt2.real,num_sqrt2.imag))


# Python 二次方程
# import cmath
# # ax**2 + bx + c = 0
# a = 1
# b = -1
# c = 0
# d = (b**2) - 4*a*c
# sol1 = (-b-cmath.sqrt(d))/(2*a)
# sol2 = (-b+cmath.sqrt(d))/(2*a)
# print('solution:',sol1,sol2)


#Python 计算三角形的面积
# a = 1
# b = 1
# c = 1
# s = (a+b+c)/2
# area=(s*(s-a)*(s-b)*(s-c))**0.5
# print('area:',area)


# Python 最大公约数算法
# def hfc(x,y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1,smaller+1):
#         if(x%i ==0and y%i==0):
#             hcf=i#这是会更新的
#     return hcf
# num1 = 5
# num2 = 9
# print(hfc(num1,num2))



# Python 最小公倍数算法
# def lcm(x,y):
#     if x > y:
#         greater = x
#     else:
#         greater = y
#     while(True):
#         if((greater%x==0) and (greater%y==0)):
#             lcm = greater
#             break
#         greater+=1
#     return lcm
# num1 = 3
# num2 = 4
# print(lcm(num1,num2))

# Python 质数判断
# num = 12
# if num > 1:
#     for i in range(2,num):
#         if(num%i)==0:
#             print('not prime')
#             break
#     else:
#         print('is prime')
# else:
#     print('not prime')



#Python 阶乘实例
num = 0
factorial = 1
if num < 0:
    print('has not factorial')
elif num == 0:
    print('is 1')
else:
    for i in range(1,num+1):
        factorial *= i
    print('factorial is',factorial)
















