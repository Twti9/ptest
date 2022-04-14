#开发者：罗地观生
#开发时间：2021/9/12 18:41
'''x = float(input("输入一个实数："))
def f(x):
    if x==0:
        print("f({:.1f})={:.1f}".format(x,x))
    elif x!=0:
        print("f({:.1f})={:.1f}".format(x,1/x))
f(x)'''
# 本题目要求计算下列分段函数_f_(x)的值：
x=float(input())
if x==0:
    print('f(%.1f)=%.1f'%(x,x))
else:
    print('f(%.1f)=%.1f'%(x,1/x))