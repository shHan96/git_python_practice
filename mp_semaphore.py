## mutiprocessing.Semphore
## 프로세스를의 실행 갯수 제한
## acquire(), release()
## 내부에 카운터 있다. -- 프로세스 실행 개수를 제한 하기 위한 것

# import multiprocessing
# import time

# def pro1(s):
#     s.acquire()
#     for i in range(4):
#         print(f'{multiprocessing.current_process().name}:{multiprocessing.current_process().pid} 작동중..')
#         time.sleep(1)
#     s.release()

# def pro2(s):
#     s.acquire()
#     for i in range(4):
#         print(f'{multiprocessing.current_process().name}:{multiprocessing.current_process().pid} 작동중..')
#         time.sleep(1)
    
#     s.release()

# if __name__ == '__main__':
#     sema = multiprocessing.Semaphore(1) # 카운터값 1
#     p1 = multiprocessing.Process(target=pro1, args=(sema,))
#     p2 = multiprocessing.Process(target=pro2, args=(sema,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

############################################################
import multiprocessing
import time

def worker_process(semaphore,index):

    semaphore.acquire()
    print(f"Worker process {index} start")
    time.sleep(1)

    print(f'Worker process {index} completed')
    time.sleep(1)
    print(f"프로세스 {index}: semaphore를 release했습니다.")
    semaphore.release()
   


if __name__=='__main__':
    semaphore = multiprocessing.Semaphore(2)

    processes = []
    for i in range(4):
        process = multiprocessing.Process(target=worker_process,args=(semaphore,i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    
    print('All processes completed')