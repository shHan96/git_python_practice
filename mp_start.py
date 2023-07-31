############프로세스를 시작하는 방법 2가지
# 스폰(spawn)방식,  포크방식(fork)

# 1)스폰 방식: 코드로 프로세스 생성 : ex) window, linux, macOS
# 2)포크 방식:  부모 프로세스를 복제해서 생성. 프로세스 생성 빠름.
# 빠르지만 그러나, 복제 시 메모리상의 코드와 수많은 데이터가 한꺼번에 복제 되므로써 시스템에 부하를 줌
# 리눅스,맥OS는 지원 윈도우에서 지원안함
################# 예제 코드 ################################
import multiprocessing

def start_process():
    return 1


# 메인코드 부분
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=start_process)
    p1.start()

    print(multiprocessing.get_start_method())

    #spawn 방식으로 프로세스가 생성딘다는 것을 알 수 있다.
    
    # 리눅스는 기본이 포크방식이고, spawn방식으로 설정하기 위해서
    # 아래와 같이 설정할 수 있다.
    #multiprocessing.set_start_method("spawn")

#########프로세스를 생성하는 3번째 방법############

# forkserver : 많은 서버가 있을 경우 중앙에 물어봐서 프로세스를 생성
# ex> linux, MacOS

# multiprocessing.set_start_mehod('forkserver')








