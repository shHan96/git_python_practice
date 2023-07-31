import multiprocessing
import time
def pro1(b,pn):
    b.wait()
    print(f'{pn} : 실행되었습니다.')

def pro2(b,pn):
    time.sleep(2)
    b.wait()
    print(f'{pn} 이 실해되었습니다.')

if __name__=='__main__':
    barrier = multiprocessing.Barrier(2)
    p1 = multiprocessing.Process(target=pro1,args=(barrier,"p1"))
    p2 = multiprocessing.Process(target=pro2,args=(barrier,"p2"))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
