#开发者：罗地观生
#开发时间：2021/9/14 19:59
# 本题要求将输入的任意3个整数从小到大输出。​
'''a,b,c=map(int,input().split())
if a>b:
    temp=a
    a=b
    b=temp
if a>c:
    temp=a
    a=c
    c=temp
if b>c:
    temp=b
    b=c
    c=temp
print("%d->%d->%d"%(a,b,c))'''
print(*sorted(map(int,input().split())),sep="->")