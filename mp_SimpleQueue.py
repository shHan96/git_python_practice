#####프로세스 간의 객체(데이터) 공유: SimpleQueue
from multiprocessing import SimpleQueue, Process
from time import sleep


def pro1(sq):
    for i in range(10):
        sq.put(i)
        print(f'simpleQueue에 {i}를 담았습니다.')
        sleep(0.5)


# 심플 큐에 있는 데이터를 가져오는 함수
def pro2(sq):
    items = []
    while True:
        item = sq.get()
        if item is None:
            print("simpleQueue에 내용을 모두 가져왔습니다. 끝")
            break
        print(f'simpleQueue의 값: {item}')
        items.append(item)
    print(items)


if __name__=="__main__":
    squeue = SimpleQueue()

    p1 = Process(target=pro1,args=(squeue,))
    p2 = Process(target=pro2,args=(squeue,))

    p1.start()
    p2.start()
    p1.join()
    squeue.put(None)
    p2.join()