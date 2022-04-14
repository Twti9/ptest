#开发者：罗地观生
#开发时间：2021/10/6 21:37
'''英文辅音字母是除A、E、I、O、U以外的字母。本题要求编写程序，统计给定字符串中大写辅音字母的个数。'''
'''str=input()
count=0
s='AEIOU'
for i in str:
    if i not in s and i>='A'and i<='Z':
        count+=1
print(count)'''
str=input()
s='AEIOU'
count=0
for i in str:
    if i.isupper()==1 and i not in s:
        count+=1
print(count)
