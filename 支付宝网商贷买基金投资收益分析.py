'''
思路1：使用支付宝网商贷买基金。

网商贷利率为万五，意思是借1万块，每天有5块钱利息。那么借30天利息为150块。
那么月利率就是1.5%。

支付宝基金买入费率为：0.15%，
        赎回费率为：0天<=持有天数<7天：1.5%，
                  7天<=持有天数<30天：0.75%，
                  30天<=持有天数<365天：0.5%，
                  365天<=持有天数<730天：0.25%，
                  730天<=持有天数：0%

那么，投资基金，如果月收益达到2.4%即可盈利！

'''

wsdrate=0.0005#网商贷利率为万五
mrrate=0.0015#支付宝基金买入费率为0.15%

def syrate(dkdate):
    cydate=dkdate-3
    wsdfee=round(wsdrate*dkdate,5)
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
    jjrate=round(mrrate+shrate,5)
    syrate=round(wsdfee+jjrate,5)
    #print ("思路一：网商贷贷款",dkdate,"天，基金持有",cydate,"天的成本收益率为",syrate,"，高于此值就盈利了！")
    return syrate

#syrate(45)

'''
思路二：用信用卡套现方式买基金

信用卡套现费率为0.65%+3
为了安全起见，我们以信用卡的最低还款期为投资时间。信用卡还款期最短为：30天。

支付宝基金买入费率为：0.15%，
        赎回费率为：0天<=持有天数<7天：1.5%，
                  7天<=持有天数<30天：0.75%，
                  30天<=持有天数<365天：0.5%，
                  365天<=持有天数<730天：0.25%，
                  730天<=持有天数：0%

那么，投资基金，如果月收益达到2.4%即可盈利！

'''
txrate=0.0065

def zdcbrate(zddate):
    cydate=zddate-3
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
    jjrate=round(mrrate+shrate,5)
    zdcbrate=round(txrate+jjrate,5)
    #print("思路二：信用卡套现，最低还款期为",zddate,"天，则成本收益率为",zdcbrate,"，达到此收益率即可盈利！")
    return zdcbrate

#zdcbrate(45)

def cb(t,tzje):
    if (syrate(t) < zdcbrate(t)):
        c="网商贷方案"
    else:
        c="信用卡套现方案"
    sy=syrate(t)*tzje
    tx=zdcbrate(t)*tzje
    print ("网商贷方案投资成本为",sy,"，信用卡套现方案投资成本为",tx)
    print ("投资",tzje,"元，投资",t,"天的最佳方案为：",c)

i=1
while i==1: 
    t=int(input("请输入投资天数："))
    if(t<=3):
        print ("小提示：借款天数必须大于3天，请重新输入")
        continue
    else:
        tzje=int(input("请输入投资金额："))
    cb(t,tzje)






    
