#-*- coding: utf-8 -*-
#python2.7
#korbit API를 이용한 자동주문넣기 버전 0.00.1
#with slack의 도움
#help C [pointResult.c]
import requests, json
import time
import datetime
import os

class KorbitValue():
    def create(hoi,mode,lastVal,accessToken,wannaKrwVal,wannaBtcVal,nonce,cancelId,refreshTokenStr): #생성
        korbitObj = KorbitValue()
        korbitObj.hoi = hoi
        korbitObj.mode = mode
        korbitObj.lastVal = lastVal
        korbitObj.accessTokenStr = accessTokenStr
        korbitObj.wannaKrwVal = wannaKrwVal
        korbitObj.wannaBtcVal = wannaBtcVal
        korbitObj.nonce = nonce
        korbitObj.cancelId = cancelId
        korbitObj.refreshTokenStr = refreshTokenStr
        return korbitObj
    def accessToken(self): #at얻기
        payload = {'client_id': 'YourID', 'client_secret': 'YourSecret','username':'YourEmail','password':'YourPassword','grant_type':'password'}
        r = requests.post("https://api.korbit.co.kr/v1/oauth2/access_token", data=payload)
        datastore = json.loads(r.text)
        temp = datastore['access_token']
        self.accessTokenStr = temp
        self.refreshTokenStr = datastore['refresh_token']
        return temp
    def refreshToken(self): #at갱신
        payload = {'client_id': 'YourID', 'client_secret': 'YourSecret','refresh_token':str(self.refreshTokenStr),'grant_type':'refresh_token'}
        r = requests.post("https://api.korbit.co.kr/v1/oauth2/access_token", data=payload)
        print("refresh token >>> ")
        print(r.text)
        datastore = json.loads(r.text)
        temp = datastore['access_token']
        self.accessTokenStr = temp
        self.refreshTokenStr = datastore['refresh_token']
        return temp
    def gettingLast(self): #최근체결가 ... 여기의 lastValue는 self.lastVal과는 별개이다.
        lastValue = 0
        for i in range(1, self.hoi):
            print(i)
            valueReq = requests.get("https://api.korbit.co.kr/v1/ticker?currency_pair=btc_krw")
            print(">>> btc value - 마지막 체결가 <<<")
            btcVal = json.loads(valueReq.text)
            print(btcVal['last'])
            time.sleep(1)
            lastValue = int(btcVal['last'])
        return lastValue
    def doFakeReq(self): 
        valueReq = requests.get("https://api.korbit.co.kr/v1/ticker?currency_pair=bch_krw")
        time.sleep(1)
    def requestBuyOrder(self): #매수주문 내자
        runCMD = 'curl -D - -X POST -H "Authorization: Bearer '+self.accessTokenStr+'" -d "currency_pair=btc_krw&type=limit&price='+str(self.wannaKrwVal)+'&coin_amount='+str(self.wannaBtcVal)+'&nonce='+str(self.nonce)+'" https://api.korbit.co.kr/v1/user/orders/buy'
        print("runCMD >> 매수주문")
        print(runCMD)
        os.system(runCMD)
    def requestSellOrder(self): #매수주문 내자
        runCMD = 'curl -D - -X POST -H "Authorization: Bearer '+self.accessTokenStr+'" -d "currency_pair=btc_krw&type=limit&price='+str(self.wannaKrwVal)+'&coin_amount='+str(self.wannaBtcVal)+'&nonce='+str(self.nonce)+'" https://api.korbit.co.kr/v1/user/orders/sell'
        print("runCMD >> 매수주문")
        print(runCMD)
        os.system(runCMD)

    def requestCancelOrder(self): #매수주문 내자
        runCMD = 'curl -D - -X POST -H "Authorization: Bearer '+self.accessTokenStr+'" -d "currency_pair=btc_krw&id='+str(self.cancelId)+'&nonce='+str(self.nonce)+'" https://api.korbit.co.kr/v1/user/orders/cancel'
        print("runCMD >> 매수주문")
        print(runCMD)
        os.system(runCMD)
    def requestMyKRWWalletInfo(self):#KRW Only
        # curl -D - -H "Authorization: Bearer $ACCESS_TOKEN" https://api.korbit.co.kr/v1/user/balances
        retVal = 0
        payload = {}
        headers = {'Authorization':self.accessTokenStr}
        r = requests.get("https://api.korbit.co.kr/v1/user/balances", headers=headers)
        if r.status_code == '200':
            resp = json.loads(r.text)
            #print(resp)
            retVal = int(resp['krw']['available'])
        else:
            retVal = -1
        return retVal
    def requestMyBTCWalletInfo(self):#KRW Only
        # curl -D - -H "Authorization: Bearer $ACCESS_TOKEN" https://api.korbit.co.kr/v1/user/balances
        retVal = 0
        payload = {}
        headers = {'Authorization':self.accessTokenStr}
        r = requests.get("https://api.korbit.co.kr/v1/user/balances", headers=headers)
        if r.status_code == '200':
            resp = json.loads(r.text)
            #print(resp)
            retVal = int(resp['btc']['available'])
        else:
            retVal = -1
        return retVal
    def getNonceNo(self):
        retVal = 0
        f = open("nonce.txt", 'r')
        retVal = f.readline()
        f.close()
        return retVal
    def setNonceNo(self):
        retVal = KorbitValue
        f = open("nonce.txt", 'w')
        f.write(str(self.nonce))
        f.close()
        return retVal
    def getAmountPoint(self):
        retVal = KorbitValue
        f = open("pointResult.txt", 'r')
        retVal = f.readline()
        f.close()
        return retVal
        

checkSalt = -1
print("Auto Korbit v0.00.001 - By HIT!")
sendMessage = False
myTotalKrw = 0
korbitObj = KorbitValue()
nonce = int(korbitObj.getNonceNo())
#여기서 미리 잔고를 구해보자
payload = {}
aToken = korbitObj.accessToken()
print("토큰")
print(aToken)
korbitObj.mode = 'NULL'
isRefreshTime = 0
while checkSalt < 0:
    if isRefreshTime > 300:
        isRefreshTime = 0
        accessTokenStr = korbitObj.refreshToken()
        korbitObj.doFakeReq()
    else:
        accessTokenStr = korbitObj.accessToken()
    if isRefreshTime > 0 :
        if isRefreshTime % 400 == 0:
            os.system('./slack_message.sh -h https://hooks.slack.com/services/TG0D5J9QU/yourDir -c general -u dandyhani2010 -i penguin -m "생존신고"'+datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
    korbitObj.hoi = 3
    try:
        lastVal = korbitObj.gettingLast()
    except:
        print("error")
    print(">>미체결내역 <<<")
    payload = {}
    authStr = 'Bearer '+accessTokenStr
    headers = {'Authorization':authStr}
    isRefreshTime = isRefreshTime + 1
    # print("authStr>>"+authStr)
    datastore2=''
    try:
        r2 = requests.get("https://api.korbit.co.kr/v1/user/orders/open", data=payload,headers=headers)
        datastore2 = json.loads(r2.text)
        print(datastore2)
    except:
        datastore=''
    if len(datastore2) > 0:
        #미체결있음모드es
        #현재 미체결의 type을 알아내자. 매수주문 미체결 인지? 매도 주문의 미체결 인지...
        typeStr = datastore2[0]['type'] #typeStr이 ask => 매도주문의 미체결, bid => 매수 주문의 미체결
        if typeStr == 'ask':
            korbitObj.mode = 'SELL'
            print('아 쫌 팔자.....')
            michegylIntVal = int(datastore2[0]['price']['value']) #type : unicode to int
            gap = michegylIntVal- lastVal
            # print(michegylInt - lastVal)
            if michegylIntVal - lastVal < 0:
                if sendMessage == False:
                    os.system('./slack_message.sh -h https://hooks.slack.com/services/TG0D5J9QU/yourDir -c general -u dandyhani2010 -i penguin -m "팔렸습니다. 확인해 보세요."')
                    sendMessage = True
        else:
            korbitObj.mode = 'BUY'
            michegylIntVal = int(datastore2[0]['price']['value']) #type : unicode to int 
            gap = michegylIntVal - lastVal
            # print(michegylIntVal - lastVal)
            if michegylIntVal - lastVal > 0:
                if sendMessage == False:
                    os.system('./slack_message.sh -h https://hooks.slack.com/services/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 -c general -u dandyhani2010 -i penguin -m "샀습니다. 확인해 보세요."')
                    sendMessage = True
#            else:
#                if michegylIntVal - lastVal < -60000:
#                    korbitObj.cancelId = str(datastore2[0]['id'])
#                    korbitObj.requestCancelOrder()
#                    korbitObj.mode = 'SELL'
    else: #미체결내역없음. 이전에 걸어둔 미체결이 체결되면 여기로 온다.
        lastVal = korbitObj.gettingLast()
        runCmd =  'curl -D -CURLOPT_HEADER -H "Authorization: Bearer '+accessTokenStr+'" https://api.korbit.co.kr/v1/user/balances > wallet.txt'
        os.system(runCmd)
        
        f = open("wallet.txt", 'r')
        walletJson = f.readline()
        f.close()
        #btc가 남았는지? KRW가 남았는지 wallet 정보로 판단한다.
        walletDic= json.loads(walletJson)
        btcAvail=float(walletDic['btc']['available'])
        if btcAvail > 0:
            korbitObj.mode = 'BUY' #잔고가 남은상태 - 팔아야 한다...->
        #korbitObj.wannaBtcVal = str(walletDic['btc']['available'])
        else:
            korbitObj.mode = 'SELL'

        if korbitObj.mode == 'NULL':
            myTotalKrw = korbitObj.requestMyKRWWalletInfo() #KRW만 구함 사용가능한...
            print('내돈>>>')
            print(myTotalKrw)
            if myTotalKrw > 0:
                korbitObj.mode = 'SELL'
            else:
                korbitObj.mode = 'BUY'
        if korbitObj.mode == 'SELL': #매도주문 미체결이 끝나서 온 경우라면? ===> 팔렸으니까 쌀떄 산다는 주문을 내자. 체결가에 50,000원 빼고 내기
            print("팔렸음 >> 매수 주문을 냅니다.")
            if int(lastVal) - 10000 > 0:
                korbitObj.wannaKrwVal = int(lastVal) - 10000
                krwAvail=float(walletDic['krw']['available'])
                # requestAmount = str(format(int(myTotalKrw)/int(korbitObj.wannaKrwVal), '.8g'))
                # print("매수요청 Amount : "+requestAmount)
                runCMD = str('./pointResult '+str(krwAvail)+' '+ str(korbitObj.wannaKrwVal)+' > pointResult.txt')
                print("runCMD >> 매수주문")
                print(runCMD)
                os.system(runCMD)
                time.sleep(0.5)
                requestAmount = korbitObj.getAmountPoint()
                korbitObj.wannaBtcVal = requestAmount
                #nonce는 파일에서 읽어오자.
                nonce=nonce+1
                korbitObj.nonce = nonce
                retVal = korbitObj.requestBuyOrder()
                print(retVal)
                korbitObj.setNonceNo()
                messageSlack = str('매수주문완료]'+str(korbitObj.wannaKrwVal)+'원,갯수:'+str(korbitObj.wannaBtcVal))
                print('messageSlack : '+messageSlack)
                toSlackRun = './slack_message.sh -h https://hooks.slack.com/services/TG0D5J9QU/yourDir -c general -u dandyhani2010 -i penguin -m '+str(messageSlack)
                os.system(toSlackRun)
            korbitObj.mode = 'BUY'
        else: #매수주문 미체결이 끝나서 온경우 ==> 샀으니까 비쌀떄 판다는 주문을 내자. 체결가에 50,000원을 더해서 내자.
            print("샀음 >> 매도 주문을 냅니다.")
            myTotalBTCDic = json.loads(walletJson) #BTC만 구함 사용가능한...
            myTotalBTC = myTotalBTCDic['btc']['available'] #BTC만 구함 사용가능한...
            korbitObj.wannaKrwVal = int(lastVal) + 10000
            korbitObj.wannaBtcVal = myTotalBTC
            if float(myTotalBTC) > 0:
                #nonce는 파일에서 읽어오자.
                nonce = nonce+1
                korbitObj.nonce = int(nonce)
                retVal = korbitObj.requestSellOrder()
                print(retVal)
                korbitObj.setNonceNo()
                messageSlack = str('매도주문완료]'+str(korbitObj.wannaKrwVal)+'원,갯수:'+str(korbitObj.wannaBtcVal))
                print('messageSlack : '+messageSlack)
                toSlackRun = './slack_message.sh -h https://hooks.slack.com/services/TG0D5J9QU/yourDir -c general -u dandyhani2010 -i penguin -m '+str(messageSlack)
                os.system(toSlackRun)
            korbitObj.mode = 'SELL'
        sendMessage = False

