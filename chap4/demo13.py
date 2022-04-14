#开发者：罗地观生
#开发时间：2021/10/6 21:51
'''本题要求编写程序，读入5个字符串，按由小到大的顺序输出。'''
# str=list(map(int,input().split()))
str=list(map(str,input().split()))
str.sort()
print("After sorted:")
for i in str:
    print(i)