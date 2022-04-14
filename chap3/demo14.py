#开发者：罗地观生
#开发时间：2021/9/15 19:51
#对两个正整数m和n（m<=n）编写程序，计算序列和m^2+1/m+(m+1)^2+1/(m+1)+...+n^2+1/n
m,n=map(int,input().split())
sum=0
for i in range(m,n+1,1):
    sum=i**2+1/i+sum
print("sum={:.6f}".format(sum))