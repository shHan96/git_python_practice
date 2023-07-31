# # 멀티프로세싱에서 프로게스 간의 공유자원을
# # 접근할 때 한번에 한 프로세스만 접근하도록 하는 Lock()
# # 데이터를 공유할 때 프로세스간의 경쟁을 방지하여 데이터에 접근하도록 함.
# import multiprocessing
# import time
# def pro1(v,lck:multiprocessing.Lock):
#     lck.acquire()
#     while v.value<10:
#         print(f"현재의 증가 값은 {v.value}")
#         v.value+=1
#         time.sleep(0.1)
#     lck.release()

# def pro2(v,lck):
#     lck.acquire()
#     while v.value> -10:
#         print(f"현재 감소값은 {v.value}")
#         v.value-=1
#         time.sleep(0.1)
#     lck.release()


# if __name__=='__main__':

#     value = multiprocessing.Value('i',0)
#     lock = multiprocessing.Lock()

#     p1 = multiprocessing.Process(target=pro1, args=(value,lock))
#     p2 = multiprocessing.Process(target=pro2,args=(value,lock))
#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

# 멀티프로세싱에서 프로게스 간의 공유자원을
# 접근할 때 한번에 한 프로세스만 접근하도록 하는 Lock()
# 데이터를 공유할 때 프로세스간의 경쟁을 방지하여 데이터에 접근하도록 함.
import multiprocessing
import time
def pro1(v,lck:multiprocessing.Lock):

    while v.value<1000000:
        print(f"현재의 증가 값은 {v.value}")
        v.value+=1
        

    

def pro2(v,lck):

    while v.value> -1000000:
        print(f"현재 감소값은 {v.value}")
        v.value-=1
        



if __name__=='__main__':

    value = multiprocessing.Value('i',0)
    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=pro1, args=(value,lock))
    p2 = multiprocessing.Process(target=pro2,args=(value,lock))
    p1.start()
    p2.start()

    p1.join()
    p2.join()