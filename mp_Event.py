# Event() 클래스: 프로세스 동기화. 프로세스를 동시에 실행하도록 할 수 있다.
# 여러 프로세스가 어떤 신호에 의해서 실행 되도록 함
# ex) sleep 메소드를 이용해 1초 뒤 두개의 프로세스가 동시에 실행하도록 할 수 있다.

import multiprocessing
import time
def pro1(evt):
    evt.wait()
    print(f"p1 프로세스입니다.")

def pro2(evt):
    evt.wait()
    print(f"p2 프로세스 입니다.")

if __name__ == "__main__":
    event = multiprocessing.Event()
    p1 = multiprocessing.Process(target=pro1, args=(event,))
    p2 = multiprocessing.Process(target=pro2,args=(event,))
    p1.start()
    p2.start()
    time.sleep(3)
    event.set()
    p1.join()
    p2.join()
    
