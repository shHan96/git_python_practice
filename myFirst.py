# 자료형
#######숫자#####
#1) 정수(int)
#2) 실수(float)
#3) 복소수(complex) ex) a = 1+2j
# a = 1 + 2j
# print(type(a)) # compley a변수의 자효형은 무엇인지 출력해

# a = 1
# print(type(a)) # int
# a  = '파이썬 드디어 시작'
# print(type(a)) # str 문자열
# print(a) # a의 내용을 출력
# a =100
# print(type(a))
# #print(len(a)) # a는 길이가 얼마야? 오류
# #int(정수)는 길이를 젤 수 없다. 숫자는 길이가 없다
# a  = '파이썬 드디어 시작' #문자열은 "",''로 표현
# print(len(a))
# print(type(a)) # 문자열은 길이를 젤 수 있다. 
# b = "큰따옴표도 문자열"
# print(type(b))
# print(b) # 문자열은 인덱스 값을 가짐, 배열
# b[0],b[1],b[2]....# 형태로 저장됨
# a = 1.1
# print(type(a)) # float
# x = 3
# print(id(x)) # 140704213754728 객체의 주소값
# 변수에 저장되는 것은 실제값이 아니고 객체의 주소이다
# a = "안녕하세요"
# print(a[0]) # 안
# print(a[3]) # 세
# print(a[-1]) # 요
# print(a[-2]) # 세
# print(a[-4]) # 녕
# print(a[5]) # 변수에 저장된 문자열은 인덱스값이 0부터 4까지 존재해요
# print(a[0:3]) #안녕하 인텍스 0:3은 0~2까지만 출력됨
# print(a[:]) # 안녕하세요 ... 처음부터 끝까지 출력
# print(a[::2]) #안하요. 처음부터 끝까지 2자리씩 건너뛰고 출력

# a = "1,2,3,4,5,6,7,8, 9"
# print(len(a)) # 쉼표도 문자열의 길이에 포함되므로 17이 나온다
# print(a[::2])
# b = "987654321"
# print(b)
# print(b[::-1]) # 123456789 역순 출력

############문자열 함수
# a = "abcd"
# print(type(a)) #str
# print(a.find("b")) # 인덱스값 1을 반환함
# print(a.replace('b',"$$"))
# print(a.find("a"))
# print(a[::-1])
# print(a) # replace()함수를 수행 후 a변수에 저장되지는 않음
# print(a.split("b"))
#help(a.find) # 문법 확인 --more 부분 클릭 후 엔터... 다음페이지까지봄
# a = "abc"
# print(a.replace("b","~"))
# a = a.replace("b","~")
# print(a)
# c  = 12345
# # print(type(c))
# # print(str(c))
# c = str(c) #int -> str 변환하고 c변수에 저장
# print(type(c)) # str
# print()
# a = "안녕하세요\
#     \n제 이름은 한상훈입니다.\
#     \n잘부탁드립니다."
# a = """안녕하세요
# 제 이름은 한상훈입니다.
# 잘부탁드립니다."""
# print(a)

# print(5+3)
#print(3-2)
# b = 5 + 3
# print(b)

# c = 3-1
# print(c)

# print(4*3)
# print(type(9/3)) # float 3.0
# print(5/3)
# print(int(5/3))
# print(5//3)
# print(5%3) # 5를 3으로 나눈 나머지 값만 출력
# print(5**3) # 5의 3제곱
# ################################################
# # 대입연산자 : (+=, -=, *=, /=, %=, **=)

# # 대입 연산자
# a = 5
# a += 3 # a를 3증가해라 , a = a + 3
# print(a)
# a -=2
# print(a) # adptj 2fmf Qorl a = a - 2

# b = 5
# b **= 3
# print(b) # b = b ** 3
# #divmod() 함수
# print(divmod(5,3))  # 5를 3으로 나누어라 결과값: (1,2) 몫은 1 나머지 2
# #pow() 함수 제곱근
# print(pow(5,1)) # 5의 3제곱 

# 그 외의 cos,sin,tan 등 계산시 제공되는 모듈 : math

# import math # math 모듈 불러들임
# # 모듈 속에는 여러개의 함수가 선언 되어 있고

# print(math.sqrt(4)) # 제곱근을 구하는 함수

##########################리스트(list: []) 값 변경이 가능하다.
# 임의의 객체 아무값이나 순서대로 저장하는 집합형태의 자료형
# a = [1, 2, 3, 4]
# print(type(a)) # 
# print(a)

# a = [1,2,[1,1.1],'a']
# 리스트의 여러가지 함수
# a = [4,1,3,2] # 리스트 데이터
# a.append(5) # 끝에
# print(a)
# a.remove(2)
# print(a)
# a.sort()
# print(a)
# a = [1,2,[1,1,2],'a']
#a[2].remove(2)
# print(a)

# a = [4,1,3,2]
# a.append(8)
# a.append(7)
# a.remove(2)
# a.remove(4)
# a.sort()
# print(a[::-1])
# print(a) # 역순 출력은 리스트값을 반환하지 않는다.
# a.reverse() # 리스트의 값을 변화 시킨다.
# print(a) 

# b = 0b11
# print(type(b))
# print(b)
# c = 0o12
# print(type(c))
# print(c)
# d = 0X23 # 접두어 0x는 16진수를 나타낸다
# print(type(d))
# print(d)

# a = 1234534738917519739438197943473891
# print(type(a))
# b  = 2e-4 # 소수 자리가 4자리 늘어남
# print(type(b))
# print(b)

#### 문자열, 자료형, 문자열 연산 ######
# a ='1'
# print(type(a)) # str
# b = "Hello, world!"
# print(type(b)) # str
# print('1'+'2')
# a = "Hello! "
# b = 'world'
# print(a+b) # a와 b가 문자열이므로 *는 문자열 연결 연산자로 작용한다

# print('2'*3) # 222 반복연잔자
# print(2*3)

# a = '안녕하세요'
# print(a[::-1])

# a = '12345'
# b = '34567'
# c = a[0:3]+b[1:]
# print(c)
# a = 'abcdefghijklmnopqrstuvwxyz'
# print(a.upper())
# a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(a.lower())
# a = 'abCFefgHi'
# print(a.swapcase()) # 대소문자가 바뀜
# a = 'abcde'
# print(a.replace('cd','1'))
# a = ['a','b','c']
# print(a)
# print('#'.join(a))

# a = 'abcd abcd'
# print(a.capitalize()) # 맨앞자기 대문자
# print(a.title()) # 단어별로 첫번째 글자가 대문자가 됨
# a = '       abcd efg     '
# print(a.strip()) # 앞뒤(좌우) 공백제거
# print(a.lstrip()) # 좌측 공백제거
# print(a.rstrip()) # 우측 공백제거
# a = "abcdef"

# print(a.find("e"))
# print(a.find("g"))

# li = list()
# print(li,type(li))

# li = [1,2,3,4,5,6,7,8,9]
# print(li[0]) #1
# print(li[len(li)-1])
# li[1]=99
# li[2]='문자'
# print(li) # 리스트 값은 문자, 숫자, 군집자료형 모두 들어갈 수 있음

######## 군집자료형: 튜플 ##############
# 튜플 : 자료 값의 변경 불가
# 소괄호()
#t = (1,2,3) # 튜플
#print(t,type(t))

# a = [1,2,3]
# a[0] = 4
# print(a)
# a = (1,2,3)
# a[0] = 4
# print(a) # TypeError 튜플은 데이터를 변경할 수 없다

# a = 1,2,3,4
# print(type(a))
# print(a)

# li = [1,2,3]
# tu = (1,2,3) # 튜플
# print(li, type(li))
# print(tu,type(tu))
# print(li[0],li[0:2])
# print(li)
# print(li+li)
# print(tu+tu) # 일시적으로 
# print(tu[1:3])
# print(li)


######################군집자료형 딕셔너리##############
# 중괄호 { K : V}
# 키는 변경 불가한 객체
#a = {'key':'value', 1 : [1,2,3], (1,2):{}}\


# d = {1:1,
#      'a' :[1, 2, 3],
#      (1,2):"aaa"
#      }
# print(d)




# a = {1,2,3,4} # set(집합)

# a = [1,2,1,1,1,1,1,2,4,2,3,3,4,5,6,7,8,0,0,2]
# a.sort()
# print(a)
# print(set(a))
# print(list(set(a)))

# s1 = set([1,2,3,4,5,6])
# print(type(s1))
# s2 = set([4,5,6,7,8,9])
# print(s1)
# print(s2)


# print(s1&s2)
# print(s1|s2)




# s = {1,2,3}
# s.add(4)
# print(s)
# s.discard(2)
# s.update([5,6])

# print(s)

# set1 = {1,2}
# set2 = {3,4}
# set1.update(set2)
# print(set1)
# print(dir(dict))

# T = (1,2,3,4,5,6,7,8)
# T = list(T)
# T[0]=0
# T.append(9)
# T.remove(8)
# T = tuple(T)
# print(T)
# a = [4,6,2,1,8,5,3,2,8,9,6]
# a.sort()
# print(a)
# a.reverse()
# print(a)
# a.sort(reverse=True)
# print(a)
# a = list(set(a))
# a.sort()
# print(a)

# print(5+3)
# print(5//3)
# print(5**3)
# print(5%3)
# print(5/3)
# print(divmod(5,3))

#a = '안녕하세요\n한상훈입니다.\n잘 부탁드립니다.' 
""" 
원하는 형태로 출력하기 위한 내요우추가
"""
# print(a)
# a = """안녕하세요.
# 홍길돌입니다.
# 잘 부탁드립니다."""
# print(a)
# print('오'+5)

# d = {'이름':'홍길동','주소':'파주시','전화':'010-0000-0000'}
# print(d['이름'])
# print(d['주소'])
# print(d['전화'])
# print(d.keys())
# print(d.values())
# print(d.items())

########### 조건문 ###############
# if (조건), while(조건):
# bool(자료형), 참(1- True) 거짓(0 - False)

# a = True
# print(type(a))
# b= False
# print(type(b))

# print(bool([1,2,3]))
# print(bool("abcd"))
# print(bool(""))
# print(bool([]))
# print(bool({"a":1 ,"b":2}))
# print(bool((1,2,3)))
# print(bool(1))
# print(bool(0))
# print(bool(()))
# print(1 == 1)
# print(1 == 2)
# print(2>0)
# print(2<1)
# b = True
# a = False
# print(a and b)
# print(not a)

# print(a or b)


# a = 1
# b = 2
# print(a>0 and b > 1)
# print(a==0 or b !=1)
# print('a' and 'b')
# print('a' or 'b')   

# #if(조건문) : 조건문이 참일 때 내용 수행
# if (True):
#     print(1) # 1

# print(2) # if문과 무관한 출력

# if(True):
#print(1) #IndentationError
#print(2)

# score = 93

# if score > 90:
#     print('A') #A
# if score > 80:
#     print('B') #B
# if score > 70:
#     print('C') #C

# score = 73
# if 100 >= score >= 90:
#     print('A')
# if score >=80 and score < 90:
#     print('B')
# if score >= 70 and score < 80:
#     print('C')

#elif 조건1 : elif 조건2  else: ....

# score = 90
# if score >=90:
#     print('A')
# elif score >= 80:
#     print('B')
# else: # 나머지 조건을 모두 포함
#     print('C')

# a = 2
# if (a==1):
#     print(1)
# elif(a==2):
#     print(2)
# else:
#     print(4)

# a = 3
# b =2
# if (a==1):
#     if b ==1:
#         print(1)
#     else:
#         print(2)
# else:
#     print(3)

# a =1
# b =4
# if (a==1):
#     if(b==3):
#         if( a<b):
#             print(0)
#         print(1)
#     else:
#         print(2)
# else:
#     print(3)

# a = 1
# if(a==1):
#     msg = 'a is 1'
# else:
#     msg = 'a is not 1'
# print(msg)


##########위의 문장을 조건부 표현식

# msg2 = 'a is 1' if(a ==1) else 'a is not 1'
# print(msg2)

########for문##########

# import collections.abc

# obj = [1,2,3,4]
# obj2 = {1,2,3,4}
# obj3 = "abcdef"
# obj4 = {'a': 'b','b':'aa','C':3 }
# obj5 = (1,2,3,4)
# obj6 = range(10)
# obj7 = range(1,10)




# print(isinstance(obj2,collections.abc.Iterable))

# ld  =list(range(10))
# print(ld)
# ld2 = ['a',1,[1,2,3],('a','b')]
# len(ld2)
# print(range(len(ld2)))


# for i in ld2:
#     print(i)

# for i in range(len(ld2)):
#     print(ld2[i])

# for j in (1,2,3,4):
#     print(j,end=',')

# for i in [1,2,3,4]:
#     print(i,end='-')

# for i in [1,2,3,4]:
#     for j in (1,2,3,4):
#         print(j,end='.')
#     print(i,end='-')


# num = 5
# while num > 0:
#     print(num)
#     num -=1

# num =1
# while num<10:
#     print(num)
#     num+=1
#     if num == 3:
#         continue
#     if num == 5:
#         break


########input()#########


######
# a = int(input("첫번째 값을 입력하시요: "))
# b = int(input("두번째 값을 입력하시요: "))
# if b==0:
#     b = int(input("0은 안됩니다. 다시 입력해주세요 : "))
# print(a,"+",b,"=",a+b)
# print(a,"-",b,"=",a-b)
# print(a,"*",b,"=",a*b)
# print(a,"//",b,"=",a//b)

#####파이썬 파일 입출력######
### 파일 입출력 #### 
#open(파일경로,모드) = 모드: 읽기,쓰기,수정

# f = open("./a.txt","w")
# f.write("1234")
# f.close()

# f = open("a.txt","a")
# f.write("5678")
# f.seek()

# f = open("C:\\pythonProject\\test\\a.txt","w")
# f.write("진짜로 잘되지...")
# f.close()

# f = open("C:\\pythonProject\\test\\a.txt","r") # 읽기 모드
# print(f.read())
# f.close()

#####################파이썬 함수#############
# 함수: 입력 ---> 처리 ----> 출력
#def 함수명():
    #실행할 코드
    
# def func(): # func() 이라는 함수 선언
#     print(1)

# func()

# def func():
#     """숫자를 출력해주는 함수 입니다""" #함수의 기능정의 가능. help(func)을 부르면 나타남
#     print(1)
    
# func() # 함수 호출부
# help(func) # 기능 정의된 내용이 출력된다.

# def gugu():
#     "구구단 2단을 출력하는 함수 입니다."
#     for i in range(1,10):
#         print(f'2 x {i} = {2*i}') # formating 방법 f"{}"


 
# def gugu():
#     "구구단 3단을 출력하는 함수 입니다."
#     for i in range(1,10):
#         print(f'3 x {i} = {3*i}') # formating 방법 f"{}"

# help(gugu)
# gugu()

###### 함수의 매개변수 ########
# def func(x): # x는 매개변수

# def gugu(x): # parameter
#     for i in range(1,10):
#         print(f'{x} x {i} = {x*i}')
        
# gugu(3) # 3은 인자값(argument) 
# # argument의 개수는 parameter의 개수와 일치해야한다.

# def gugu(x=2): # default값 세팅
#     for i in range(1,10):
#         print(f'{x} x {i} = {x*i}')
        
# gugu(5)
# gugu()

# def func(x,y,z,a,b=0,c=1):
#     print(f'{x}==x, {y}==y , {z}==z, {a}==a, {b}==b, {c}==c')

# func(1,2,3,4,5,6)

# b = [1, 2,3]
# def func2():
#     b = [4,2,3]
#     b[0]=4
#     print(b)
# func2()
# print(b)


# ###############if문 응용, 리스트와 함께 사용 #############
# fruit = ['사과','배','딸기','포도']
# fruit.append("귤")
# print(fruit)

# if '딸기' in fruit: #fruit 리스트 속에 아이템 딸기가 잇으면
#     print("딸기가 있네요.^^")
    
############### 포매팅 print() ########################
#print("...%d %f %s %x...." % )
# %는 좌우를 구분하는 용도
# 서식
# %d : 정수 %x(정수 16진수) ,%o (8진수)
# 2) 실수 : %f(소수점이 붙은 실수)
# 3) %c : 한글자, %s는  (두글자 이상의 문자열)

# print("%d" % 123)
# print("%5d" % 123)    
# print("%05d" % 123 )
# print("{0:d} {1:5d} {2:05d}".format(123,456,789))

###############이스케이프 문자#############
# \n:엔터
# \t: 텝키
# \b: 백스페이스
# \\: \
# \': '
# \": "

# print("\n줄바꿈\n연습")
# print("\t탭키\t연습")
# print("글자가 \"깅조\"되는 효과1")
# print('글자가 \'깅조\'되는 효과2')
# print("\\\\\\")

# def func1():
#     result = 100
#     return result

# def func2():
#     print("반환값이 없는 함수 실행")
    
    
# hap = 0

# hap = func1()

# print("func()에서 돌려준 값 : %d"% hap)
# func2()

# # 군집자료형을 쓰는 이유 중 하나는 반환값이 여러개인 함수인 경우에 사용
# # 함수는 문법상 리턴 값이 두개 이상일 수가 없다.
# # 리스트의 반환할 값을 넣은 후 리스트 변수를 리턴하면 문법상 오류가 없어진다.

# def sum():
#     pass # 예약어 이고 아무 기능도 하지 않디만 실행코드 대신 써서 오류처리

############모듈 #############
#1) 표준 모듈
#2) 사용자 모듈
#3) 외부 모듈

# import turtle ## 파이썬 표준 모듈 (내장) - Turtle graphic
# t = turtle.Turtle() #turle.Turtle() 거북이 인스턴스 생성(객체), 거북이를 그를 컴버스도 생성
# t.shape("turtle") # 거북이 모양 형성
# t.forward(100) # 전진 100
# turtle.exitonclick() #프로그램 종료를 위해서 클릭시 캔버스 닫침

#파일명은 모듈명과 같지 않도록 주의!!

# t = turtle.Turtle()
# t.shape('turtle')
# for i in range(4):
#     t.forward(100)
#     t.right(90)
# t.color('red', 'yellow')
# t.begin_fill()
# while True:
#     t.forward(200)
#     t.left(170)
#     if abs(t.pos()) < 1:
#         break
# t.end_fill()
# t.done()
# turtle.exitonclick()

# import turtle

# t = turtle.Turtle()
# t.speed(100)
# t.shape("arrow")
# t.color("yellow")
# t.begin_fill()
# for i in range(500):
#     t.forward(200)
#     t.left(12)
# t.end_fill()
# turtle.exitonclick()


# import sys
# print(sys.builtin_module_names)

# import math
# print(dir(math))

# import calendar
# print(calendar.calendar(2023))


# import time
# # print(time.ctime())
# # print(time.time())
# # print(1)
# # time.sleep(5)
# # print(2)

# for i in range(1,10):
#     print(i)
#     time.sleep(1)        

#### 시간 내에 단어 입력하는 프로그램
# import time
# word = 'cookie'
# start_time = time.time()
# answer = input("cookie를 입력해주세요.")
# end_time = time.time()
# if word == answer and (end_time-start_time) <5:
#     print('정답')
# else:
#     print("오답")
    
# import random # 무작위 숫자를 뽑아준다, 0~1까지의 숫자

# words = ['cookie','apple','banana'] # 0~2까지
# print(random.choice(words))
# print(random.choice(words))
# print(random.choice(words))

# a = range(1,10) #1부터 9까지 무작위 숫자를 3번 추출
# print(random.choice(a))
# print(random.choice(a))
# print(random.choice(a))

# print(int(random.random()*3))
# print(words[int(random.random()*3)])

# words = ['cookie','apple','banana','melon','blueberry']
# print(words[int(random.random()*5)])


################클래스###############################
# class Car: #Car 클래스 시작
#     #자동차의 필드 : 클래스 속의 변수
#     color = "" # 필드1
#     speed = 0 # 필드2
    
#     def upSpeed(self, value): # 메소드1 # self는 클래스 자기자신
#     # self는 클래스의 변수를 참조 하기 위하여 사용하는 매개변수
#         self.speed += value # self.speed = self.speed + value
#         #매개변수 value값을 전달 받은 값을 기존의 speed에 추가하라
#     def downSpeed(self ,value):
#         self.speed -= value
    
#메인코드 부분: 인스턴스 생성, 메서드 호출.............
# myCar1 = Car() # 클래스 객체를 생성하고 myCar1이라는 이름을 붙임

# myCar1.color = "빨강" # 생성하고 myCar1이라는 이름을 붙임
# myCar1.speed = 0    # 생성된 인스턴스의 필드(변수) 영역이 만들어짐

# myCar2 = Car() # 인스턴스 생성
# myCar2.color = "파랑"
# myCar2.speed = 0

# myCar3 = Car() # 인스턴스 생성
# myCar3.color = "노랑"
# myCar3.speed = 0

# myCar1.upSpeed(30)     
# print("자동차1의 색상은 %s이며, 현재 속도는 %d km입니다" % (myCar1.color,myCar1.speed))

# myCar2.upSpeed(60)
# print("자동차2의 색상은 %s이며, 현재 속도는 %d km입니다"% (myCar2.color,myCar2.speed))                      

# myCar3.upSpeed(0)
# print("자동차3의 색상은 %s이며, 현재 속도는 %d km입니다"% (myCar3.color,myCar3.speed))                      
      
    


# 클래스 선언
# class Car:
#     color = ""
#     speed = 0
    
#     def __init__(self):
#         self.color = "빨강"
#         self.speed = 0
    
#     def upSpeed(self,value):
#         self.speed +=value
#     def downSpeed(self, value):
#         self.speed -=value
        
# #메인 코드 부분
# myCar1 = Car()
# myCar2 = Car()

# print("자동차1의 색상은 %s이며, 현재 속도는 %d입니다."% (myCar1.color,myCar1.speed))
# print("자동차2의 색상은 %s이며, 현재 속도는 %d입니다."% (myCar2.color,myCar2.speed))




#클래스 선언
# class Car:
#     color = "" # 인스턴스 변수
#     speed = 0  # 인스턴스변수
    
#     def __init__(self,value1,value2): # 두개의 매개변수
#         self.color = value1 
#         self.speed = value2
        
#     def upSpeed(self,value):
#         self.speed +=value
#     def downSpeed(self, value):
#         self.speed -=value
        
        
# myCar1 = Car("빨강",30)
# myCar2 = Car("파랑",60)

# print("자동차1의 색상은 %s이며, 현재 속도는 %d입니다."% (myCar1.color,myCar1.speed))
# print("자동차2의 색상은 %s이며, 현재 속도는 %d입니다."% (myCar2.color,myCar2.speed))



# class Car:
#     color = "" #인스턴스 변수1: 메서드 안의 지역변수
#     speed = 0 #인스턴스 변수2:
#     count = 0 #클래스변수 # 클래스 전체의 전역변수
    
#     def __init__(self):
#         self.speed = 0
#         Car.count +=1 # Car.으로 변수를 부르면 클래스 변수인
        
        
# # 변수 선언 부분
# myCar1, myCar2 = None,None

# myCar1 = Car()
# myCar1.speed =30

# print("자동차1의 현재 속도는 %dkm,생산된 자동차는 총 %d대 입니다." %(myCar1.speed,Car.count))
# myCar2 =Car()
# myCar2.speed=60
# print("자동차1의 현재 속도는 %dkm,생산된 자동차는 총 %d대 입니다." %(myCar2.speed,Car.count))


######### 메서드 오버라이딩 : 서브클래스에서 슈퍼클래스의 메서드를 저장한다

# class Car:
#     speed = 0
#     def upSpeed(self,value):
#         self.speed +=value

#         print("현재 속도(슈퍼클래스): %d " % self.speed)
        
# class Sedan(Car): # 슈퍼클래스 Car를 상속받음
#     def upSpeed(self, value):
#         self.speed +=value
#         if self.speed > 150:
#             self.speed =150
#             print("현재 속도(서브 클래스):%d " % self.speed)
            
# class Truck(Car):
#     pass # 슈퍼 클래스의 모든 내용을 그대로 상속받음, 재정의 없음

# #변수 선언 부분
# sedan1,truck1 = None, None

# #메인 코드 부분: 인스턴스 생성, 메서드 호출 등
# sedan1 = Sedan() # Sedan()설계도로부터 sedan1을 생성
# truck1 = Truck()

# print('승용차 -->',end="")
# sedan1.upSpeed(200)

# print("트럭-->",end="")
# truck1.upSpeed(200)

###### 특별한 메서드를 #############
# class Line:
#     length = 0
#     def __init__(self, length) -> None:
#         self.length = length # 매개변수 length값을 self.length에 저장
#         print(self.length,"길이의 선이 생성되었습니다.")
    
#     def __del__(self): #인스턴그가 삭제될 때 호출되는 메서드
#         print(self.length, "길이의 선이 삭제되었습니다.")
    
#     def __repr__(self) -> str: #print(메서드)
#         return "선의 길이: " + str(self.length)
    
#     def __add__(self,other):
#         return self.length + other.length
    
#     def __lt__(self,other): # <
#         return self.length<other.length
    
#     def __eq__(self,other):
#         return self.length == other.length
    

# # 메인 코드 부분

# myLine1 = Line(100)
# myLine2 = Line(200)

# print(myLine1)

# print("두 선의 길이 합:",myLine1+myLine2)     

# if myLine1 < myLine2: # __lt__()호출
#     print("선분 2가 더 기네요.")
# elif myLine1 == myLine2: #__eq__()
#     print("두 선분의 길이가 같네요.")
# else:
#     print("모르겠네요.")
    
# del myLine1
# del myLine2

# class SuperClass:
#     def method(self):
#         pass # 추상 클래스
    
# class subClass1(SuperClass):
#     def method(self):
#         print("SubClass에서 method()를 오버라이딩함")
        
# class subClass2(SuperClass):
#     pass # 나중에 심각한 오류발생 가능성 있음 --> 오버라이딩 필요!

# ## 메인 코드 부분 ##
# sub1 = subClass1()
# sub2 = subClass2()

# sub1.method() # SubClass1에서 method()를 오버라이딩 함
# sub2.method() # 메서드 오버라이딩이 안되었으므로 아무것도 출력안됨

#### 메소드 오버로딩######################
# 같은 이름의 메소드를 중복해서 사용

# class Calculator:
#     def add(self, a, b):
#         """
#         두 수를 더하는 메소드입니다.
#         :param a:숫자
#         :param b:숫자
#         :return:두수의 합
#         """
#         return a+b
    
#     def add(self, a, b, c=0): # 매개변수 3개짜리 add()
#         """
#         두 수를 더하는 메소드입니다.
#         :param a:숫자
#         :param b:숫자
#         :param c:숫자
#         :return:세 수의 합
#         """
#         return a + b + c
    
# calc = Calculator()
# result1 = calc.add(2,3)
# print("두 수 의 합: ",result1)

# result2 = calc.add(2,3,4)
# print(result2)


####################################################################
## 모듈을 import 여러가지 방법
#import 모듈명
# import multiprocessing
# print(multiprocessing.cpu_count())
#모듈명의 별칭
# import multiprocessing as mt
# print(mt.cpu_count())


#from 모듈명 import * : 모듈속에 모든 클래스, 메서드, 변수 등을 가져옴
# from multiprocessing import *
# print(cpu_count())


# from multiprocessing import cpu_count
# print(cpu_count())

# 함수를 별칭처리
# from multiprocessing import cpu_count as cc
# print(cc())


# from 모듈명 import 변수명
# from multiprocessing import current_process
# print(current_process().name )

# from multiprocessing import current_process, cpu_count
# print(cpu_count())
# print(current_process().name)



# #함수와 변수 import시에 별칭 처리
# from multiprocessing import cpu_count as cc, current_process as cp
# print(cc())
# print(cp().name)

# from multiprocessing import Process, freeze_support


# # 클래스 선언 부분
# class HelloProcess(Process): #Process 클래스 상속
#     def __init__(self,argu1,argu2): # 생성자 메서드
#         super(Process,self).__init__() # 슈퍼 클래스의 Process클래스의 생성자 호출
        
        
#     def run(self) -> None:
#         print("Hello Process2")
        
        
        
# #메인 코드 부분

# if __name__ == "__main__":
    
#     freeze_support() # 윈도우에서의 멀티프로세싱할 때 필요
#     p1 = HelloProcess(1,argu2="hello") # 프로세스의 객체 생성
#     p1.start()
#     p1.join()
#     p1.terminate() # 생략가능

# # 함수로 4개의 프로세스를 생성하는 프로그램
# import multiprocessing
# def worker_processing(name):
#     # 각 프로세스의 작업을 정의합니다.
#     print(f'Worker process {name} started')
    
# if __name__ == "__main__":
#     num_processes = 4
    
#     processes = []
    
#     for i in range(num_processes):
#         p = multiprocessing.Process(target=worker_processing,args=(i,))
#         p.start()
#         processes.append(p) # 프로세스를 리스트에 추가
        
        
#     for p in processes:
#         p.join()
        
#     print("All_proceese_completed")



