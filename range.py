for i in range(3,5):
    print("Doing important work. i =", i)


r = range(3,5)
for i in r:
    print("Doing important work. i =", i)



def double_odds(nums):
    for i, num in enumerate(nums):
        if num % 2 == 1:
            nums[i] = num * 2

x = list(range(10))
double_odds(x)
print(x)






l = list(enumerate(['a', 'b']))
print(l)

l2 = list(['a', 'b'])
print(l2)
















