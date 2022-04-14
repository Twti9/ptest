#开发者：罗地观生
#开发时间：2021/10/4 21:55
'''
输入一个以#结束的字符串，本题要求滤去所有的非十六进制字符（不分大小写），组成一个新的表示十六进制数字的字符串，然后将其转换为十进制数后输出。如果在第一个十六进制字符之前存在字符“-”，则代表该数是负数。

'''
str=input()
flag=1
res=""
checked=False
for i in str:
    if (i>='0'and i<='9')or(i>='A'and i<='F')or(i>='a' and i<='f'):
        res+=i
        checked=True
    elif i=='-'and checked==False:
        flag=-1
if res=='':
    print(0)
else:
    print(flag*int(res,16))