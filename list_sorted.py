def count_negatives(nums):
    nums.append(0)
    # We could also have used the list.sort() method, which modifies a list, putting it in sorted order.
    nums = sorted(nums)
    return nums.index(0)




test_nums = [-2,5,-3,8,22]
print(test_nums)

print(count_negatives(test_nums))
print(test_nums)









