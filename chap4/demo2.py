#开发者：罗地观生
#开发时间：2021/9/15 20:40
'''给定两个整数_A_和_B_，输出从_A_到_B_的所有整数以及这些数的和'''
A,B=map(int,input().split())
j=0
Sum=0
if -100<=A<=B<=100:
    for i in range(A,B+1):
        print("%5.d" % i, end="")
        j=j+1
        Sum=Sum+i
        if(j%5==0):
            print("\n",end="")
        elif(i==B):
            print("\n",end="")
print("Sum= %d"%Sum)