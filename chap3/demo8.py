#开发者：罗地观生
#开发时间：2021/9/13 20:35
# 本题要求编写程序，计算序列 1 + 1/3 + 1/5 + … 的前N项之和。​
N=int(input("输入一个正整数:"))
sum=0
for i in range(1,N+1):
    sum=1/(2*i-1)+sum
print("sum={:.6f}".format(sum))