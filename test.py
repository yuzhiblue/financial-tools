#测试页面

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
    
    print ("赎回费率",shrate)

syrate(5)
