#开发者：罗地观生
#开发时间：2021/9/13 20:42
# 本题要求编写程序，计算交错序列 1-2/3+3/5-4/7+5/9-6/11+… 的前N项之和。
N=int(input("输入一个正整数："))
sum=0
for i in range(1,N+1):
    sum=((-1)**(i+1))*(i/(2*i-1))+sum
print("{:.3f}".format(sum))
'''n=int(input())
sum=0
 for i in range(1,n+1):
     if i%2==0:
        sum-=(i/(2*i-1))
    else:
        sum+=(i/(2*i-1))
print("{:.3f}".format(sum))
'''