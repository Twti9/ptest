#开发者：罗地观生
#开发时间：2021/9/15 20:13
'''本题要求编写程序，根据输入的三角形的三条边_a_、b、c，计算并输出面积和周长。注意：在一个三角形中， 任意两边之和大于第三边。三角形面积计算公式：area=√_s_(s_−_a)(s_−_b)(s_−_c)，其中_s_=(a+b+c)/2。'''
import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
if(a+b<=c or a+c<=b or b+c<=a):
    print("These sides do not correspond to a valid triangle")
else:
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("area=%.2f"%area,"perimeter=%.2f"%(s*2))
