#开发者：罗地观生
#开发时间：2021/10/6 21:58
'''对于给定的正整数N，求它的位数及其各位数字之和。
​'''
str=input()
m=len(str)
sum=0
for i in str:
    sum=sum+int(i)
print("{:d} {:d}".format(m,sum))