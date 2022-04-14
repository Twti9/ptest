#开发者：罗地观生
#开发时间：2021/10/3 10:40
'''本题要求统计一个整型序列中出现次数最多的整数及其出现次数。
​'''
a=input().split()[1:]#从第二个字符开始
d={}
for b in set(a):#调用set函数把a字符串转成单个字符的值进行插入，保证唯一性
    d[a.count(b)]=b
max_count=max(d.keys())#调用keys函数取出字典的键
max_number=d.get(max_count)#根据键取值
print('{} {}'.format(max_number,max_count))