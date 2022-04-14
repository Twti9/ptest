#开发者：罗地观生
#开发时间：2021/9/13 20:10
'''a,n=map(int,input("输入2个9以内的正整数：").split())
sum=0
s=0
for i in range(n):
    s=s+a*(10**i)
    sum=sum+s
print("s=",sum)'''
# 给定两个均不超过9的正整数_a_和_n_，要求编写程序求_a_+aa+aaa++⋯+aa_⋯_a（n_个_a）之和。
a,n=map(int,input().split())
num=0
sum=0
for i in range(1,n+1):
    num=num*10+a
    sum+=num
print("s =",sum)


