from multiprocessing import JoinableQueue,Process
from time import sleep
def pro1(q:JoinableQueue,pn):
    for i in range(100):
        q.put(i)
        print(f"{pn} : jq에 값을 {i}를 입력했습니다.")
        sleep(0.1)

def pro2(q:JoinableQueue,pn):
    items = []
    while True:
        item = q.get()
        q.task_done()
        if item is None:
            print("모든 jq객체의 데이터르 가져왔습니다.")
            break
        items.append(item)
        print(f"{pn} : jq객체로 부터 {item}을 가져왔습니다")
        print(items)
    q.task_done()  # 카운ㅌ가 없으므로 작업의 종료를 알려줘야 한다.


if __name__ == "__main__":
    q = JoinableQueue()
    p1 = Process(target=pro1, args=(q,"p1"))
    p2 = Process(target=pro2,args=(q,"p2"))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    