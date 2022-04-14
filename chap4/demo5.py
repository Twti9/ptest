#开发者：罗地观生
#开发时间：2021/9/21 13:29
'''输入一个字符串，再输入两个字符，求这两个字符在字符串中的索引。'''
str=input()
count=len(str)-1
checkCode=list(input().split())
while count>=0:
    if str[count]==checkCode[0] or str[count]==checkCode[1]:
        print("{:d} {:s}".format(count,str[count]))
    count=count-1