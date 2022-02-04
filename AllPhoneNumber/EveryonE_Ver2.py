
import os
import time
import datetime

#파일쓰기 가능버전
#sqlite3 기준 SQL을 생성한다.
#이것의 실행 결과물을 적용하기 전에 아래 create 문을 생성해서, userInfo Table을 먼저 생성해야 한다.
#create table userInfo (id integer, phoneNo text, memo text);


def printLogo():
    print("+--------------------+")
    print("+  EveryonE + SQL    +")
    print("+--------------------+")
    print("|  Ver : 0.01.0      |")
    print("|  By  : HanIT       |")
    print("| Create: 2022.01.03 |")
    print("+--------------------+")

def makeCreateSQL():
    f = open("createUserInfo.sql", 'w')
    sql = f'create table userInfo (id integer, phoneNo text, memo text);'
    f.write(sql)
    f.close()
    
def makeSQL(count, item):
    return f'insert into userInfo values ({count}, {item}, "test");'

    #출처: https://araikuma.tistory.com/706 [프로그램 개발 지식 공유]

#화면 Clear
os.system('clear')
print("")

#화면 Logo 출력
printLogo()

#SQL : create 구문 파일 작성
makeCreateSQL()

#Body 시작 준비
stTime = datetime.datetime.now()
count=0
f = open("result.log", 'w')
createData = ""
for j in range(0,10000):  #1,10000
    for i in range(0,10000): #1,10000
        if j < 10:  
            if i < 10:
                createData = '010-000'+str(j)+'-000'+str(i)
                #print('010-000'+str(j)+'-000'+str(i))
                #data = createData + "\r\n"
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
            elif i>=10 and i < 100:
                createData = '010-000'+str(j)+'-00'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-000'+str(j)+'-00'+str(i))
            elif i>=100 and i < 1000:
                createData = '010-000'+str(j)+'-0'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-000'+str(j)+'-0'+str(i))
            else:
                createData = '010-000'+str(j)+'-'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-000'+str(j)+'-'+str(i))
        if j >= 10 and j < 100:  
            if i < 10:
                createData = '010-00'+str(j)+'-000'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-00'+str(j)+'-000'+str(i))
            elif i>=10 and i < 100:
                createData = '010-00'+str(j)+'-00'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-00'+str(j)+'-00'+str(i))
            elif i>=100 and i < 1000:
                createData = '010-00'+str(j)+'-0'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-00'+str(j)+'-0'+str(i))
            else:
                createData = '010-00'+str(j)+'-'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-00'+str(j)+'-'+str(i))
        if j >= 100 and j < 1000:  
            if i < 10:
                createData = '010-0'+str(j)+'-000'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-0'+str(j)+'-000'+str(i))
            elif i>=10 and i < 100:
                createData = '010-0'+str(j)+'-00'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-0'+str(j)+'-00'+str(i))
            elif i>=100 and i < 1000:
                createData = '010-0'+str(j)+'-0'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-0'+str(j)+'-0'+str(i))
            else:
                createData = '010-0'+str(j)+'-'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-0'+str(j)+'-'+str(i))
        if j >= 1000 and j < 10000:  
            if i < 10:
                createData = '010-'+str(j)+'-000'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-'+str(j)+'-000'+str(i))
            elif i>=10 and i < 100:
                createData = '010-'+str(j)+'-00'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-'+str(j)+'-00'+str(i))
            elif i>=100 and i < 1000:
                createData = '010-'+str(j)+'-0'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-'+str(j)+'-0'+str(i))
            else:
                createData = '010-'+str(j)+'-'+str(i)
                data = makeSQL(count, createData) + "\r\n"
                f.write(data)
                #print('010-'+str(j)+'-'+str(i))
        count = count + 1
#        if count % 100000 == 0:
#            print(".", end = "")
f.close()
print("finish")
#print(stTime)
then = datetime.datetime.now()
#print(datetime.datetime.now())
duration = then - stTime
resultSec = duration.total_seconds()
sec = resultSec
#print(resultSec)
min=0
if resultSec > 60:
    min = resultSec / 60
    sec = resultSec - (int(min) * 60)
    #print(min,end = "")
result = f'Start : {stTime}, finish : {then}'
print(result)

result2 = f'During : {int(min)}min {int(sec)}sec.'
print(result2)

result3 = f'Count : {count}(s) '
print(result3)

fsize = os.path.getsize("result.log")

result4 = f'Logfile size : {fsize} bytes.'
print(result4)

#print(count)
