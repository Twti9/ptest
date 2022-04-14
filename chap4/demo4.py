#开发者：罗地观生
#开发时间：2021/9/20 18:22
'''一个合法的身份证号码由17位地区、日期编号和顺序编号加1位校验码组成。校验码的计算规则如下：

首先对前17位数字加权求和，权重分配为：{7，9，10，5，8，4，2，1，6，3，7，9，10，5，8，4，2}；然后将计算的和对11取模得到值Z；最后按照以下关系对应Z值与校验码M的值：
Z：0 1 2 3 4 5 6 7 8 9 10
M：1 0 X 9 8 7 6 5 4 3 2
'''
def judge(id,weight,checkCode):
    sum=0
    index=0
    freWords=id[:17]
    lastWord=id[-1]
    for i in freWords:
        if i<'0' or i>'9':
            return False
        else:
            sum=sum+weight[index]*int(i)
            index+=1
    sum=sum%11
    if checkCode[sum]==lastWord:
        return  True
    else:
        return False

m=int(input())
count=0
weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
checkCode=['1','0','X','9','8','7','6','5','4','3','2']
x=[]
for i in range(m):
    id=input()
    if judge(id,weight,checkCode)==False:
        x.append(id)
    else:
        count+=1
if count==m:
    print("All passed")
for i in x:
    print(i,end="\n")
