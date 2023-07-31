## Pipe() 클래스: multiprocessing.Pipe
## 데이터를 공유하는 객체
## 메모리(RAM)를 기반으로 데이터 공유
## Pipe() 는 객체 공유를 메모리를 기반으로 하기 때문에 사용가능한
## 시스템 메모리의 한계에 따라 제한될 수 있다. 즉, 시스템의 물리적 메모리인 RAM이 부족하면 파이프를 통해 전달되는
## 데이터 용량에 제한을 받을 수 있다.

## 대용량 데이터 공유를 위해서는 Queue나 Manager를 이용!

import multiprocessing


def pro1(sender):
    sender.send('1234') # send() 메서드에 보내는 데이터는 반복 가능한 객체
    print("p1 데이터를 보냈습니다")

def pro2(receiver):
    item =receiver.recv() # 데이터를 받는 메소드
    print(f'p2가 {item}를 받았습니다.')
if __name__ == '__main__':
    sender, receiver = multiprocessing.Pipe()  
    p1 = multiprocessing.Process(target=pro1,args =(sender,))
    p2 = multiprocessing.Process(target=pro2, args = (receiver,))

    p1.start()
    p2.start()
    print(multiprocessing.current_process())
    print(f"current process name: {multiprocessing.current_process().name}")
    print(f'current process id : {multiprocessing.current_process().pid}')
    # 실행 중인 자식 프로세스 리스트 출력
    active_processes = multiprocessing.active_children()
    print("active_processes")
    for i in active_processes:
        print(f'Name : {i.name} pid : {i.pid}')
    p1.join()
    p2.join()

