#开发者：罗地观生
#开发时间：2021/10/6 22:15
'''本题要求编写程序，将给定字符串中的大写英文字母按以下对应规则替换：'''
'''def change(word):
    return chr(ord('A')+25-(ord(word)-ord('A')))
s=input()
ans=""
for i in s:
    if  i>='A' and i<='Z':
        ans+=change(i)
    else:
        ans+=i
print(ans)'''
s=input()
ans=[]
for i in s:
    if 'A'<=i<='Z':
        ans.append(chr(155-ord(i)))
    else:
        ans.append(i)
print("".join(ans))

