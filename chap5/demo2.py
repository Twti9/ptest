"""时间处理相关方法:最终目的是获得一个str类型的时间"""
import time
import datetime
'''在给定时间类型字符串的情况下，直接输出或者更改格式后输出'''
abc = "2020/7/5 15:45:23"#输入时间类型的字符串
print(abc)#直接输出即可
abcTuple = time.strptime(abc,"%Y/%m/%d %H:%M:%S")#把时间类型字符串转成时间元组，此处格式需要与给定的时间格式一致，
otherStyleTime = time.strftime("%Y*%m*%d %H:%M:%S",abcTuple)#返回以指定可读字符串表示的当地时间，*和:可换成其他字符
print("abc_otherStyleTime:",otherStyleTime,type(otherStyleTime))

"""不给定时间类型字符串，而是直接从当前系统时间获取"""
#1、使用time模块
now = int(time.time())#调用time模块的time函数直接获取当前系统时间的时间戳,可使用int强制转换
timeTuple = time.localtime(now)#格式化时间戳为时间元组
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S",timeTuple)#此处的-和:都可以换成自己喜欢的字符
print("now_otherStyleTime:",otherStyleTime,type(otherStyleTime))
#2、使用datetime模块
now_=datetime.datetime.now()#获取当前系统时间，注意不是时间戳,不可使用int强制转换，要求必须是字符串型
otherStyleTime = now_.strftime("%Y-%m-%d %H:%M:%S")#转为指定格式,此处-和:可以换成其他字符
print("now__otherStyleTime:",otherStyleTime,type(otherStyleTime))

"""给定时间戳使用time模块或者datetime进行处理，返回str类型的时间"""
#使用time模块
timeStamp = 1557502800
timeTuple = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeTuple)
print("timeStamp_otherStyleTime:",otherStyleTime,type(otherStyleTime))
#使用datetime模块
datetimeStamp=1554846480
date_ = datetime.datetime.utcfromtimestamp(datetimeStamp)#将时间戳转为时间
otherStyleTime = date_.strftime("%Y/%m/%d %H:%M:%S")
print("date_otherStyleTime:",otherStyleTime,type(otherStyleTime))

"""获取几天前的日期"""
#使用datetime
twoDayAgo = (datetime.datetime.now() - datetime.timedelta(days=2))#先获取时间格式的日期
print(twoDayAgo)#时间后会带有6位小数
otherStyleTime = twoDayAgo.strftime("%Y-%m-%d %H:%M:%S")#转换为其他时间格式
print("twoDay_otherStyleTime:",otherStyleTime,type(otherStyleTime))
"""总结：time模块  
time.time()     获取当前系统时间的时间戳
time.localtime()将时间戳转为时间元组
time.strptime() 将字符串类型的时间转为时间元组
time.strftime() 将时间元组以指定格式返回
         datetime模块
datetime.now()  获取当前系统时间
时间.strftime() 格式化时间
"""
x="2020-1-5 15:45:32"
x1=1504548958
y1=time.localtime(x1)
print('y1=',y1)
print(time.strftime("%Y%m%d %H%M%S",y1))
y=time.strptime(x,"%Y-%m-%d %H:%M:%S")
print(y)
z=time.strftime("%Y/%m/%d %H:%M:%S",y)
print(z)
print(datetime.datetime.now().strftime("%Y*%m*%d %H:%M:%S"))
m=str(datetime.datetime.strptime("2021/1/15 15:45:32","%Y/%m/%d %H:%M:%S"))
print(m,type(m))

