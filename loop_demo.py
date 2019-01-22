# import heapq
#
#
# l = [5,222,33,124,54,1,3]
# print(l)
# heapq.heapify(l)
# print(l)
#
#
# l2 = []
# for i in range(len(l)):
#     heapq.heappush(l2,l[i])
#     print(l2)



count = 0
while count < 5:
    print('count is ',count)
    count += 1
else:
    print('count above or equals to 5')


flag = 5
# while flag:print(flag)
while flag:flag-=1

l1 = [4,43,3,323,3]
for x in l1:
    print('val is ',x)
    if x == 323:
        break
else:
    print('loop end!')

for i in range(3):
    print(i)
for i in range(3,5):
    print(i)
for i in range(0,100,33):
    print(i)
for i in range(100,0):
    print('none:',i)
for i in range(100,0,-33):
    print('not none:',i)
for i in range(-10,-100,-30):
    print('negative:',i)
for i in range(-10,-100,30):
    print('negative too?',i)
for i in range(-100,-10,34):
    print('negative too:',i)



# l1 = list(2,3,4,5)#takes 1 param but 4
l1 = list((2,3,4,5))
l2 = list(range(2,6))
print(l1)
print(l2)
print(l1==l2)

#循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。
#终于找到用处了，break就可以不执行else了，而不只是在循环后边做一个无意义的善后，其实那个根本不需要占用else

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,' equals to ',x,'*',n//x)
            break
    else:
        print(n,' is prime number')

# pass 语句
# Python pass是空语句，是为了保持程序结构的完整性。
#我的理解就是让程序块完整吧，而不是语法报错
# while True:
#     pass









