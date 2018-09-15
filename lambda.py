mod_5 = lambda x:  x % 5

print('101 mod 5 =', mod_5(101))




abs_diff = lambda a, b: abs(a - b)
print("Absolute difference of 5 and 7 is", abs_diff(5,7))



always_32 = lambda : 32
always_32()


names = ['jacques', 'TJ','tA','WTF']
print("Longest name is :",max(names))
print("Longest name is :",max(names,key=lambda name: len(name)))
print("Name sorted :",sorted(names))
print("Name sorted case insensitive:",sorted(names,key=lambda name:name.lower()))



