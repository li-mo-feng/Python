#输入某年某月某日,判断这一天是这一年的第几天.
#需要判断是否是闰年:
#以及每个月的天数
#1.3.5.7.8.10.12是31天
#2.4.6.9.11是30天
#比如1999年5月1日,那么首先闰年365,非366,然后五月
a=[30,28,31,30,31,30,31,31,30,31,30,31]
#b=[30,28,31,30,31,30,31,31,30,31,30,31]
#index=(a[int(month)+1])#判断输入月的天数

#

def run(year,month,date):
    # year=int(input("请输入今年是哪一年:"))
    # month=int(input("时输入月份:"))
    # date=int(input("请输入今天的日期:"))
    days=[30,28,31,30,31,30,31,31,30,31,30,31]
    if (year<=9999 and year>0) and (month<=12 and month>0) and (date<=31 and date>0):#判断输入的逻辑正确性
        if (year%4==0 and year%100!=0)or(year%400==0):
            print("您输入的年份是闰年")
            days[1]=29#如果是闰年二月是29日
            print(days)#显示一年每个月的实际天数
            day=sum(days[0:month])+date#计算该月是今年的第多少天
            # print(")#---------施工线
            return "且今天是今年的第%d"%day
        else:
            print("这一年不是闰年")
            print(days)  # 显示一年每个月的实际天数
            day = sum(days[0:month]) + date  # 计算该月是今年的第多少天
            return "且今天是今年的第%d" % day
    else:
        return "您输入的年份错误"



a = run(1994,11,10)

