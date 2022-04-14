#开发者：罗地观生
#开发时间：2021/10/8 20:58
a=['3','4','5','6','7','8','9','10','J','Q','K','A','2']
b=[('♣','black'),('♠','black'),('♦','red'),('♥','red')]
d=['大王','小王']
# d=[{'2':('♣','red')},]
def product(x,y):
    for i in x:
        for j in y:
            d.append(dict({i:j}))
    print(d)
product(a,b)
print(len(d))
