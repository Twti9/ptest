#开发者：罗地观生
#开发时间：2021/9/13 20:52
# 读入2个正整数A和B，1<=A<=9, 1<=B<=10,产生数字AA…A,一共B个A
'''A,B=map(int,input("输入2个正整数(1<=A<=9, 1<=B<=10)：").split(','))
x=0
for i in range(B):
    x=x+A*(10**i)
print(x)'''
a,b=map(int,input().split(','))
res=0
for i in range(1,b+1):
    res=(res*10)+a
print(res)
