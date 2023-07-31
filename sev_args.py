import multiprocessing
import time

#함수 선언부
def worker_function(name, delay):
    print(f"worker {name} 시작")
    time.sleep(delay)
    print(f"worker {name} 종료")


# 메인 코드 부분
if __name__== '__main__':

    process1 = multiprocessing.Process(target=worker_function,args=("프로세스1",2))
    #Process() 클래스로 부터 프로세스객체 생성
    process2 = multiprocessing.Process(target=worker_function,args=("프로세스2",3))

    # 프로세스 실행
    process1.start()
    process2.start()

    # 프로세스 종료대기
    process1.join()
    process2.join()

    print('모든 프로세스 종료')