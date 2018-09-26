import copy

def count_negatives(nums):
    nums.append(0)
    # We could also have used the list.sort() method, which modifies a list, putting it in sorted order.
    nums = sorted(nums)
    return nums.index(0)

def count_positives(nums):
    #way 1
    '''
    nums.append(0)
    nums = sorted(nums,reverse=True)# needs revert,if nums have 0 already
    print('sorted:',nums)
    print(nums.index(0))
'''
    #way 2 solution of waste-my-life

    # way 2.2 detect 0 first
    try:
        nums.index(0)
    except:
        nums.append(0)#still wrong, if origin nums have more zeros,
    nums = sorted(nums)

    print(nums)
    print(len(nums))
    print('positives:',len(nums)-nums.index(0) - 1)
    print(nums.index(0))



test_nums = [-2,5,-3,8,22,44,0,0]
print(test_nums)
print(test_nums.index(-2))
print(test_nums.index(5))


#print('negatives\' num:',count_negatives(test_nums))#this is not ok,it changed original list
print('negatives\' num:',count_negatives(copy.copy(test_nums)))
print('positives\' num:',count_positives(copy.copy(test_nums)))

print(test_nums)









