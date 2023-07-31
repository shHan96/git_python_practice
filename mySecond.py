
# # a = 1 + 2j
# # print(type(a))

# # a = 1
# # print(type(a))
# # a = '파이썬 드디어 시작'
# # print(type(a))
# # print(a)
# # a = 100
# # print(type(a))
# # #print(len(a))# 에러발생
# # a = '파이썬 드디어 시작'
# # print(len(a))
# # print(type(a))
# # b = "큰따옴표도 문자열"
# # print(type(b))
# # print(b)
# # a = 1.1
# # print(type(a))
# # x = 3
# # print(id(x))

# # a = "안녕하세요"
# # print(a[0])
# # print(a[3])
# # print(a[-1])
# # print(a[-2])
# # print(a[-4])
# # print(a[0:3])
# # print(a[:])
# # print(a[::2])

# # a = "1,2,3,4,5,6,7,8,9"
# # print(len(a))
# # print(a[::2])
# # b ="987654321"
# # print(b)
# # print(b[::-1])

# # a = "abcd"
# # print(type(a))
# # print(a.find("b"))
# # print(a.replace('b','$'))
# # print(a.find('a'))
# # print(a[::-1])
# # print(a)
# # print(a.split('b'))
# # help(a.find)
# # a = "abc"
# # print(a.replace("b","~"))
# # print(type(help))

# # #a = [1,2,[1,1,1],'a']
# # a = [4,2,3,1]
# # a.sort()
# # print(a)

# # a = [4,1,3,2]
# # a.append(8)
# # a = [4,1,3,2]
# # a.append(8)
# # a.append(7)
# # a.remove(2)
# # a.remove(4)
# # a.sort()
# # print(a[::-1])
# # print(a) 
# # a.reverse() 
# # print(a) 

# #b = 0b11
# # li = [1, 2, 3]
# #tu = (1, 2, 3)
# # print(li, type(li))
# # print(tu,type(tu))
# # print(li[0],li[0:2])
# # print(li)
# # print(li+li)
# # print(tu,tu)
# # print(tu[1:3])
# # print(li)




# ######################군집자료형 딕셔너리##############
# # 중괄호 { K : V}
# # 키는 변경 불가한 객체
# #a = {'key':'value', 1 : [1,2,3], (1,2):{}}\

# # d = {1:1,
# #      'a' :[1, 2, 3],
# #      (1,2):"aaa"
# #      }
# # print(d)

# # a = [ 1,2,1,1,1,1,1,1,1,2,2,2,2,2,4,4,4,4,4,5,5,6,6,6,6,6,5,5,4,4,3,2 ]

# # a.sort()
# # print(set(a))
# # print(list(set(a)))



# ######## 조건문#####
# # if(조건), while(조건):
# # bool(자료형), 참(1 - True) 거진(0 - False)

# # a = True
# # print(type(a))
# # b = False
# # print(type(b))

# # print(bool([1,2,3]))
# # print(bool("abcd"))
# # print(bool([]))
# # print(bool({"a":1, "b":2}))
# # print(bool(1))
# # print(bool(0))
# # print(bool(()))
# # print( 1 == 1)
# # print(1==2)
# # print(2>0)
# # print(2<1)
# # b = True
# # a = False
# # print(a and b)
# # print(not a)

# # print(a or b)

# # a = 1
# # b = 2
# # print(a>0 and b >1)
# # print(a==0 or b !=1)
# # print('a' and 'b')
# # print('a' or 'b')

# # if(조건문) : 조건문이 참일 때 내용 수행
# # if (True):
# # print(1) #1

# # print(2) # if문과 무관한 출력

# # if (True):
# # print(1) #IndentationError
# # print(2)

# # score = 93
# # if score > 90:
# # print('A')
# # if score > 80:
# # print('B')
# # print()

# letters = 'python'
# print(letters[0],letters[2])

# license_plate = "24가 2210"
# print(license_plate[-4:])

# string = "홀짝홀짝홀짝"
# print(string[::2])

# string = "PYTHON"
# print(string[::-1])

# phone_number = "010-1111-2222"
# print(' '.join(phone_number.split('-')))
# print(''.join(phone_number.split('-')))

# url = "http://sharebook.kr"
# print(url.split('.')[-1])

# string = 'abcdfe2a354a32a'
# print(string.replace('a','A'))


# #33
# print('-'*80)

# t1 = 'python'
# t2 = 'java'
# print((t1+' '+t2+' ')*3)

# # 35
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름: %s 나이: %d" % (name1,age1))
# print("이름: %s 나이: %d" % (name2,age2))

# # 36
# print("이름: {name} 나이: {age}".format(name=name1,age=age1))
# print("이름: {name} 나이: {age}".format(name=name2,age=age2))

# print(f'이름: {name1} 나이: {age1}')
# print(f'이름: {name2} 나이: {age2}')

# 상장주식수 = "5,969,782,550"
# print(str(''.join(상장주식수.split(','))))

# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])

# data = "   삼성전자    "
# print(data.strip())

# ticker = "btc_krw"
# print(ticker.upper())

# ticker = "BTC_KRW"
# print(ticker.lower())

# a = "hello"
# print(a.capitalize())

# file_name = "보고서.xlsx"
# print(file_name.endswith("xlsx"))

# file_name = "보고서.xlsx"
# print(file_name.endswith("xlsx") or file_name.endswith("xls"))

# file_name = "2020_보고서.xlsx"
# print(file_name.startswith("2020"))

# a = "hello world"
# print(a.split())

# ticker = "btc_krw"
# print(ticker.split("_"))

# date = "2020-05-01"
# print(data.split('-'))

# data = "039490     "
# print(data.rstrip())

# movie_rank = ["닥터 스트레인지","스플릿","럭키"]

# movie_rank.append("배트맨")
# movie_rank.insert(1,"슈퍼마켓")
# movie_rank.remove("럭키")
# print(movie_rank)

# movie_rank.remove("스플릿")
# movie_rank.remove("배트맨")
# print(movie_rank)

# #56
# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# langs = lang1+lang2
# print(langs)

# nums = [1, 2, 3, 4, 5, 6, 7]
# print("max:",max(nums))
# print("min:",min(nums))

# nums = [1, 2, 3, 4, 5]
# print(sum(nums))

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# nums = [1, 2, 3, 4, 5]
# print(sum(nums)/len(nums))

# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])

# #2
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])

# print(nums[1::2])

# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0],interest[2])

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(' '.join(interest))

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print('/'.join(interest))

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print('\n'.join(interest))

# string = "삼성전자/LG전자/Naver"
# print(string.split('/'))

# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)

# my_variable=()
# movie_rank = ("닥터 스트레인지","스플릿","럭키")
# a = (1,)
# print(a)

# t = 1, 2, 3, 4
# print(type(t))

# t = ('a', 'b', 'c')
# t = list(t)
# t[0]='A'
# t=tuple(t)
# print(t)

# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)
# print(tuple(i for i in range(1,100) if i%2==0))

# #81
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# start, expression,*valid_score = scores
# print(start, expression,valid_score)

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, start, expression = scores
# print(start, expression,valid_score)

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# start,*valid_score, expression = scores
# print(start, expression,valid_score)

# #84
# temp ={}

# #85
# 아이스크림 = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
# print(아이스크림)
# #86
# 아이스크림['죠스바']=1200
# 아이스크림['월드콘']=1500
# print(아이스크림)
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# print("메로나 가격:",ice['메로나'])

# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# ice['메로나']=1300

# ice.pop('메로나')
# print(ice)



# # 134
# print("출력", "A")
# print("출력", "B")
# print("출력", "C")

# # 135
# print("변환", "A".lower())
# print("변환", "B".lower())
# print("변환", "C".lower())

# #136
# for i in (10,20,30):
#     print(i)

# #137
# for i in range(10,31,10):
#     print(i)

# #138
# for i in [10,20,30]:
#     print(10)
#     print("-"*7)

# #139
# print("++++")
# for i in [10,20,30]:
#     print(i)

# for i in range(4):
#     print("-"*7)

# 리스트 = [100, 200, 300]
# for i in 리스트:
#     print(i+10)

# 리스트 = ["김밥", "라면", "튀김"]
# for i in 리스트:
#     print("오늘의 메뉴:",i)

# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# for i in 리스트:
#     print(len(i))

# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i,len(i))

# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i[0])

# 리스트 = [1, 2, 3]
# for i in 리스트:
#     print(3,'x',i)

# 리스트 = [1, 2, 3]
# for i in 리스트:
#     print(3,'x',i,'=',3*i)

# 리스트 = ["가", "나", "다", "라"]

# for i in 리스트[1:]:
#     print(i)

# 리스트 = ["가", "나", "다", "라"]
# for i in 리스트[::2]:
#     print(i)

# # 150
# for i in 리스트[::-1]:
#     print(i)

# 리스트 = [3, -20, -3, 44]
# for i in 리스트:
#     if i<0:
#         print(i)

# 리스트 = [3, 100, 23, 44]
# for i in 리스트:
#     if i%3==0:
#         print(i)

# 리스트 = [13, 21, 12, 14, 30, 18]
# for i in 리스트:
#     if i%3==0 and i<20:
#         print(i)

# 리스트 = ["I", "study", "python", "language", "!"]
# for i in 리스트:
#     if len(i)>=3:
#         print(i)

# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#     if i.isupper():
#         print(i)

# # 161
# for i in range(100):
#     print(i)

# for i in range(2002,2051,4):
#     print(i)

# for i in range(3,31,3):
#     print(i)

# for i in range(99,-1,-1):
#     print(i)

# for i in range(10):
#     print(i/10)

# for i in range(1,10):
#     print("3x{} =".format(i),i*3)

# for i in range(1,10,2):
#     print("3x{} =".format(i),i*3)

# a=0
# for i in range(1,11):
#     a+=i
# print(a)

# a=0
# for i in range(1,11,2):
#     a+=i
# print(a)

# a=1
# for i in range(1,11):
#     a*=i
# print(a)

# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(price_list[i])

# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(i,price_list[i])

# price_list = [32100, 32150, 32000, 32500]
# for i in range(1,len(price_list)):
#     print(100+(i-1)*10,price_list[i])

# my_list = ["가", "나", "다", "라"]
# for i in range(0,len(my_list)-1):
#     print(my_list[i],my_list[i+1])

# my_list = ["가", "나", "다", "라", "마"]
# for i in range(len(my_list)-2):
#     print(my_list[i],my_list[i+1],my_list[i+2])

# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list)-1,0,-1):
#     print(my_list[i],my_list[i-1])

# my_list = [100, 200, 400, 800]
# for i in range(len(my_list)-1):
#     print(my_list[i+1]-my_list[i])

# my_list = [100, 200, 400, 800, 1000, 1300]

# for i in range(len(my_list)-2):
#     print(sum(my_list[i:i+3])/3)

# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# volatility = []
# for i in range(len(low_prices)):
#     volatility.append(high_prices[i]-low_prices[i])
# print(volatility)

# apart =[[(100*i)+j for j in range(1,3)] for i in range(1,4)]
# print(apart)

# stock = [ ["시가", 100, 200, 300], ["종가", 80, 210, 330] ]

# stock = {'시가':[100,200,300],'종가':[80,210,330]}
# print(stock)

# stock = {'10/10':[80,110,70,90],'10/11':[210,230,190,200]}

# apart = [ [101, 102], [201, 202], [301, 302] ]

# for i in apart:
#     for j in i:
#        print(j,'호')

# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart[::-1]:
#     for j in i:
#        print(j,'호')

# apart = [ [101, 102], [201, 202], [301, 302] ]

# for i in apart[::-1]:
#     for j in i[::-1]:
#        print(j,'호')

# for i in apart:
#     for j in i:
#        print(j,'호')
#        print("-"*5)

# for i in apart:
#        for j in i:
#               print(j,'호')
#        print("-"*5)
# apart = [ [101, 102], [201, 202], [301, 302] ]

# for i in apart:
#     for j in i:
#        print(j,'호')
# print("-"*5)

# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for i in data:
#     for j in i:
#        print(j*1.00014)

# for i in data:
#     for j in i:
#        print(j*1.00014)
#     print("-"*4)

# result = [i*1.00014 for j in data for i in j]
# print(result)

# result = [[i*1.00014 for i in j] for j in data]
# print(result)

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]  
# for i in ohlc[1:]:
#     print(i[3])

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in ohlc[1:]:
#     if i[3]>150:
#        print(i[3])

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in ohlc[1:]:
#     if i[3]>=i[0]:
#        print(i[3])

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# volatility=[]
# for i in ohlc[1:]:
#     volatility.append(i[1]-i[2])
# print(volatility)

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in ohlc[1:]:
#     if i[3]>i[0]:
#        print(i[1]-i[2])

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]

# #200
# a=0
# for i in ohlc[1:]:
#     a+=i[3]-i[0]
# print(a)

# 201
# def print_coin():
#     print("비트코인")

# # 202
# print_coin()

# #203
# for i in range(300):
#     print_coin()

# #204
# def print_coins():
#     for _ in range(100):
#         print("비트코인")

#215
# def print_with_smile(s):
#     print(s+':D')

# print_with_smile("안녕하세요")

# def print_upper_price(price):
#     print(price*1.3)

# def print_sum(a,b):
#     print(a+b) 
    
# def print_arithmetic_operation(a,b):
#     print("%d + %d = %d" % (a,b,a+b))
#     print("%d - %d = %d"% (a,b,a-b))
#     print("%d * %d = %d"% (a,b,a*b))
#     print("%d / %d = %d"% (a,b,a/b))

# def print_max(a, b, c) :
#     max_val = 0
#     if a > max_val :
#         max_val = a
#     if b > max_val :
#         max_val = b
#     if c > max_val :
#         max_val = c
#     print(max_val)

# def print_reverse(s):
#     return s[::-1]

# def print_score(a):
#     return (sum(a)/len(a))

# def print_even(a):
#     for i in a:
#         if(i%2==0):
#             print(i)

# def print_keys(d:dict):
#     for i in d.keys():
#         print(i)

# def print_value_by_key(my_dict:dict,key):
#     print(my_dict.get(key))

# def print_5xn(s:str):
#     temp = len(s)//5
#     for i in range(temp+1):
#         print(s[i*5:i*5+1])

# def printmxn(s:str,n):
#     temp = len(s)//n
#     for i in range(temp+1):
#         print(s[i*n:i*n+n])
        

# printmxn("아이엠어보이유알어걸", 3)


# def calc_monthly_salary(a):
#     return a//12

# def make_url(s):
#     return "www"+s+".com"

# def make_list(s):
#     return list(s)

# def pickup_even(a):
#     return [i for i in a if i%2==0]

# print(pickup_even([3, 4, 5, 6, 7, 8]))

#241
# import datetime
# print(datetime.datetime.now())
# print(type(datetime.datetime.now()))
# for i in range(1,6):
#     print(datetime.datetime.now().date()-datetime.timedelta(i))

# now = datetime.datetime.now()
# print(now.strftime("%H:%M:%S"))

# day = "2020-05-04"
# ret = datetime.datetime.strptime(day, "%Y-%m-%d")
# print(ret, type(ret))

# import time
# for i in range(10):
#     t = datetime.datetime.now()
#     print(t)
#     time.sleep(1)

# class Human:
#     def __init__(self,name,age,gender) -> None:
#         self.name = name
#         self.age = age
#         self.gender = gender
#         print("응애응애")
        
#     def who(self):
#         print("이름:",self.name,", 나이:",self.age,", 성별:",self.gender)
    
#     def setInfo(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
    
#     def __del__(self):
#         print("나의 죽음을 알리지 마라")


# areum = Human("조아름",25,"여자")
# print(areum.age)
# areum.who()
# del areum

# class Stock:
#     def __init__(self,name,cord,per,pbr, dividend):
#         self.name = name
#         self.cord = cord
#         self.per =per
#         self.pbr = pbr
#         self.dividend = dividend
    
#     def set_name(self,name):
#         self.name = name
    
#     def set_cord(self,cord):
#         self.cord=cord
#     def set_per(self,per):
#         self.per =per
#     def set_pbr(self,pbr):
#         self.pbr =pbr
#     def set_dividend(self,dividend):
#         self.per =dividend
#     def get_name(self):
#         return self.name
    
#     def get_cord(self):
#         return self.cord
#     def get_per(self):
#         return self.per

# A = []
# A.append(Stock("삼성전자","005930",15.79,1.33,2.83))
# A.append(Stock("현대차","005380",8.70,0.35,4.27))
# A.append(Stock("LG전자","0066570",317.34,0.69,1.37))
# # stock1.set_per(12.75)

# for i in A:
#     print(i.get_cord(),i.get_per())

# import random
# class Account:
#     count =0
#     @classmethod
#     def get_account_num(cls):
#         print(Account.count)
    
    
#     def __init__(self,name,balance) -> None:
#         self.bank="SC은행"
#         self.name = name
#         self.balance = balance
#         num1 = random.randint(0,999)
#         num2 = random.randint(0,99)
#         num3 = random.randint(0,999999)
#         string = "{:03}-{:02}-{:06}".format(num1,num2,num3)
#         self.account = string
#         self.deposit_count=0
#         print(self.account)
#         Account.count+=1
    
#     def deposit(self,money):
#         if money > 0:
#             self.balance+=money
#             self.deposit_count+=1
#             if(self.deposit_count==5):
#                 balance*=1.01
#                 self.deposit_count=0
#     def withdraw(self,money):
#         if self.balance>=money:
#             self.balance-=money
            
#     def display_info(self):
#         print("은행이름 :",self.bank)
#         print("예금주:",self.name)
#         print("계좌번호:",self.account)
#         print("잔고:",self.balance)
    
# a = Account("kim",0)
# Account.get_account_num()


# class 부모:
#     def __init__(self):
#         print("부모생성")

# class 자식(부모):
#     def __init__(self):
#         print("자식생성")

# 나 = 자식()

# class 부모:
#   def __init__(self):
#     print("부모생성")

# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
#     super().__init__()

# 나 = 자식()

# from collections.abc import Callable, Iterable, Mapping
# from multiprocessing import Process, freeze_support
# from typing import Any

# def Hello():
#     print("Hello1")
    
# if __name__== '__main__':
    
#     p1 = Process(target=Hello)
#     p1.start()
#     p1.join()
#     p1.terminate()

# class Hello(Process):
#     def __init__(self):
#         super(Process,self).__init__()
        
#     def run(self) -> None:
#         print("Hello2")
        
# if __name__=="__main__":
    
#     p1 = Hello()
#     p1.start()
#     p1.join()
#     p1.terminate()

# from multiprocessing import Process

# def Hello2(i):
#     print(i,"Hello")

# if __name__ =="__main__":
#     ps = []
#     for i in range(4):
#         p = Process(target=Hello2,args=(i,))
#         p.start()
#         ps.append(p)
#     for i in range(4):
#         ps[i].join()

# from multiprocessing import Queue,Process
# import time
# def pro1(q:Queue):
#     for i in range(100):
#         q.put(i)
#         time.sleep(0.1)

# def pro2(q:Queue):
#     items = []
#     while True:
#         item = q.get()
#         if item is None:
#             print('모든 데이터를 가지고 왔습니다.')
#             break
#         items.append(item)
#         print(f"p2: q객체에서 {item}를 가져왔습니다.")
#         print(f"현재 q에 저장된 값은 {items} 입니다")

# if __name__ == "__main__":
#     queue = Queue()
#     p1 = Process(target=pro1,args=(queue,))
#     p2 = Process(target=pro2,args=(queue,))
#     p1.start()
#     p2.start()

#     p1.join()
#     queue.put(None)
#     p2.join()

# from multiprocessing import JoinableQueue,Process
# from time import sleep
# def pro1(q:JoinableQueue,pn):
#     for i in range(10):
#         q.put(i)
#         print(f"{pn} : jq에 값을 {i}를 입력했습니다.")
#         sleep(0.1)
#     q.join()
# def pro2(q:JoinableQueue,pn):
#     items = []
#     while True:
#         item = q.get()
#         if item is None:
#             print("모든 jq객체의 데이터르 가져왔습니다.")
#             break
#         items.append(item)
#         print(f"{pn} : jq객체로 부터 {item}을 가져왔습니다")
#         print(items)
#       # 카운ㅌ가 없으므로 작업의 종료를 알려줘야 한다.

# if __name__ == "__main__":
#     q = JoinableQueue()
#     p1 = Process(target=pro1, args=(q,"p1"))
#     p2 = Process(target=pro2,args=(q,"p2"))
#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

# import multiprocessing
# import time
# import sys

# def pro1(v,pn):
#     print(v)
#     print(f'{pn}:Value객체의 초기값 : {v.value}')
#     print(sys.getsizeof(v))
# def pro2(v,pn):
#     time.sleep(2)
#     v.value = 10
#     print(f'{pn}:pro2에서 입력된 값: {v.value}')
    
# ##  메인코드 부분
# if __name__=='__main__':
#     value = multiprocessing.Value('i',0) #데이터 공유를 위해 Value객체 공유
#     #데이터 공유를 위해 Value 객체 생성, i : 정수
#     p1 = multiprocessing.Process(target=pro1,args=(value,"p1"))
#     p2 = multiprocessing.Process(target=pro2,args=(value,"p2"))
#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()



