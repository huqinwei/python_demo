a, b = 0,1
while b < 1000:
    # print(b,end=',')

    #wrong
    # print(b,',')
    #wrong
    print(b,sep = ',')


    a,b=b,a+b



#wrong
print('hahahaha',sep=',')

#这个给str list不行，只能用在一个print有多个参数的情况。
l = ['a','b','c']
print(l)
print(l,sep=',')

string = 'hello'
print(string)
print(string,sep=',')

print("file\n","abc","bcd","fff\n","poi")
print("-------------")
print("file\n","abc","bcd","fff\n","poi",sep='')
print("-------------")
print("file\n","abc","bcd","fff\n","poi",sep=' ')
print("-------------")

print('a','b','c','d')
print('a','b','c','d',sep=',')
print('a','b','c','d',sep='!')
#别忘了，sep不加到最后一个“单词”的后边


print("file\n","abc","fff",sep='#########\n',end='')#空格和什么都没有是不一样的
print("....")
print("file\n","abc","fff",sep='#########\n',end=' ')#空格和什么都没有是不一样的
print(".............")
print("file\n","abc","fff",sep='#########\n',end='\n')#默认是这个，换行符，如果改成''就不换了
print("...................")
print("file\n","abc","fff",sep='#########\n')#默认是换行
print("................................")

with open('abc.txt','w') as f:
    print("file\n","abc","fff",sep='####\n',end='',file=f)