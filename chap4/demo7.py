#开发者：罗地观生
#开发时间：2021/10/3 10:23
'''本题要求提取一个字符串中的所有数字字符（‘0’……‘9’），将其转换为一个整数输出'''
'''str=input()
ans=0
for i in str:
    if i>='0' and i<='9':
        ans=ans*10+int(i)
print(ans)'''
str=input()
ans=[]
for i in str:
    if i.isdigit():
        ans.append(i)
print(int("".join(ans)))