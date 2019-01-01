for i in range(3,5):
    print("Doing important work. i =", i)


r = range(3,5)
for i in r:
    print("Doing important work. i =", i)



def double_odds(nums):
    for i, num in enumerate(nums):
        print('enumerate returns a tuple of (index,value) i:',i,' num:',num)
        if num % 2 == 1:
            nums[i] = num * 2

x = list([6,45,1213,1232,1231,23,123,22])
print('x:',x)
double_odds(x)


l = list(enumerate(['a', 'b']))
print('list of enumerate:',l)

l2 = list(['a', 'b'])
print('list:',l2)
















