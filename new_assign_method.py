a,b = 0,1
while b < 10:
        print(b)
        # a, b = b, a+b

        #wrong
        # a = b
        # b = a + b

        #right#先计算右边表达式，然后同时赋值给左边
        n = b
        m = a + b
        a = n
        b = m