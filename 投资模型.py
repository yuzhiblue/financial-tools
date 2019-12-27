#使用类的方法构建投资模型
class Touzi:
    wsdrate=0.0005#网商贷利率为万五
    mrrate=0.0015#支付宝基金买入费率为0.15%
    txrate=0.0065#套现费率为0.65%
    def __init__(self,time,money):
        self.t=time
        self.m=money
            
    def wsd(self):#网商贷方案
        cydate=self.t-3#假设基金赎回有3天时间，是不计算收益的。
        #根据时间计算基金赎回费率
        if (0<=cydate<7):
            shrate=0.015
        elif(7<=cydate<30):
            shrate=0.0075
        elif(30<=cydate<365):
            shrate=0.005
        elif(365<=cydate<730):
            shrate=0.0025
        elif(730<=cydate):
            shrate=0  
        jjrate=self.mrrate+shrate#基金总费率
        wsdcb=self.m*self.wsdrate*self.t#网商贷成本
        jjmmcb=self.m*jjrate#基金总成本
        wsdcost=wsdcb+jjmmcb
        return wsdcost
    
    def tx(self):#信用卡套现方案
        cydate=self.t-3#假设基金赎回有3天时间，是不计算收益的。
        #根据时间计算基金赎回费率
        if (0<=cydate<7):
            shrate=0.015
        elif(7<=cydate<30):
            shrate=0.0075
        elif(30<=cydate<365):
            shrate=0.005
        elif(365<=cydate<730):
            shrate=0.0025
        elif(730<=cydate):
            shrate=0  
        jjrate=self.mrrate+shrate#基金总费率
        txcb=self.txrate*self.m
        jjmmcb=self.m*(1-self.txrate)*jjrate
        txcost=txcb+jjmmcb
        return txcost

i=1
while i==1:
    print("=====================================")
    print("为了更好的为您提供投资方案，请您输入以下信息！")
    print("=====================================")
    ts=int(input("请输入投资天数："))
    if (ts<=3):
        print("基金赎回期需要3天，请输入大于3的天数。")
        continue
    else:
        if (ts>45):
            print("请注意，信用卡还款期一般不超过45天，超过45天将会产生很大误差！") 
        je=int(input("请输入投资金额："))
        fa=Touzi(ts,je)#实例化方案
        w=fa.wsd()
        x=fa.tx()
        print("网商贷方案成本为：",w,"，信用卡套现成本为：",x)
        if(w<x):
            print("综上，应该选择网商贷方案！")
        else:
            print("综上，应该选择信用卡套现方案！")
