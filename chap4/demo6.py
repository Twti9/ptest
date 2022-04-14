#开发者：罗地观生
#开发时间：2021/9/21 14:01
'''本题要求编写程序，从给定字符串中查找某指定的字符。'''
x=input()
str=input()
count=len(str)-1
while count>=0:
    if str[count]==x:
        print("index={:d}".format(count))
        break
    count-=1
if count==-1:
    print("not found")