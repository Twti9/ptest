#开发者：罗地观生
#开发时间：2021/10/3 11:00
'''本题要求编写程序，找出给定的_n_个数中的最大值及其对应的最小下标（下标从0开始）。'''
m=int(input())
integers=list(map(int,input().split()))
max_integer=max(integers)
print("{:d} {:d}".format(max_integer,integers.index(max_integer)))