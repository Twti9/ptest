#开发者：罗地观生
#开发时间：2021/9/14 20:19
'''输入2个正整数lower和upper（lower≤upper≤100），请输出一张取值范围为[lower，upper]、且每次增加2华氏度的华氏-摄氏温度转换表。
温度转换的计算公式：C=5×(_F_−32)/9，其中：_C_表示摄氏温度，_F_表示华氏温度。'''
lower,upper=map(int,input("输入2个正整数lower和upper（lower≤upper≤100）").split())
if lower<=upper<=100:
    print("fahr celsius")
    for i in range(lower,upper+1,2):
         # print("{:d}{:6.1f}".format(i,5*(i-32)/9))
         print("{:d}{:>6.1f}".format(i,5*(i-32)/9))
else:
    print("Invalid.")