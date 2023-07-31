##데이터 공유 Value클래스
import multiprocessing


def pro1(v,pn):
    print(v)
    print(f'{pn}:Value객체의 초기값 : {v.value}')

def pro2(v,pn):
    v.value = 10
    print(f'{pn}:pro2에서 입력된 값: {v.value}')
##  메인코드 부분
if __name__=='__main__':
    value = multiprocessing.Value('i',0) #데이터 공유를 위해 Value객체 공유
    #데이터 공유를 위해 Value 객체 생성, i : 정수
    p1 = multiprocessing.Process(target=pro1,args=(value,"p1"))
    p2 = multiprocessing.Process(target=pro2,args=(value,"p2"))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
