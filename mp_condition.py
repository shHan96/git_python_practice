## multiprocessing.Condition() 메소드를 통해서 프로세스 동기화
## Condition : 조건에 따라 프로세스를 실행할지 말지를 결정할 수 있도록 동기화함

# import multiprocessing

# ## 조건을 기다리다 실행하는 함수
# ## 1개의 프로세스를 동일한 건디션 객체를 이용해서 기다리게 하고 깨우는 프로그램

# def pro1(con,pn):
#     con.acquire() # 컨디션 객체를 획득
#     con.wait() # 특정 조건이 될 때까지 기다림
#     print(f" {pn} 프로세스의 기다림이 끝났습니다. pro1함수 동작 중...")
#     con.release() # 컨디션 객체를 해제

# def pro2(con): # p3가 동작감지 p1,p2 깨우는 역활
#     con.acquire()
#     #con.notify() #p1이나 p2중 임의의 프로세스를 깨움
#     con.notify_all()
#     con.release()

# if __name__ == '__main__':
#     con = multiprocessing.Condition()
#     p1 = multiprocessing.Process(target=pro1,args=(con,"p1"))
#     p2 = multiprocessing.Process(target=pro1,args= (con,"p2"))
#     p3 = multiprocessing.Process(target=pro2, args=(con,))

#     p1.start()
#     p2.start()
#     p3.start()

#     p1.join()
#     p2.join()
#     p3.join()

import multiprocessing
import time
def worker_process(condition, pn):

    with condition:
        condition.wait()
    multiprocessing.current_process().name

    print(f'{multiprocessing.current_process().pid} : {pn} Worker process started')
    print('Worker process completed')
    

if __name__ == '__main__':

    condition = multiprocessing.Condition()
    p1 = multiprocessing.Process(target=worker_process,args=(condition,"p1"))
    p2 = multiprocessing.Process(target=worker_process,args=(condition,"p2"))
    
    p1.start()
    p2.start()
    time.sleep(2)
    with condition:
        condition.notify_all()
    p1.join()
    p2.join()
    
    print('All processes completed')
