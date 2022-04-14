#开发者：罗地观生
#开发时间：2021/9/14 19:03
# 输入一个整数和进制，转换成十进制输出
m,n=map(int,input("输入一个整数和进制：").split(','))
count=0
ans=0
while(m>0):
    ans=ans+(m%10)*pow(n,count)
    count=count+1
    m=int(m/10)
print(int(ans))
'''m,n=input().split(',')
ans=int(m,int(n))
print(ans)
'''