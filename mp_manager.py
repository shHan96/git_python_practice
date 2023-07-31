###### 데이터를 공유하기 위한 객체 Manager
import multiprocessing

def pro1(ml):
    ml.append('p1')
    print(f"현재 리스트의 값: {ml}")

def pro2(ml):
    ml.append('p2')
    print(f"pro2함수에서 리스트에 값을 추가했습니다. {ml}")

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    manager_list = manager.list() # 빈 리스트 생성
    print(f'manager_list의 값: {manager_list}')
    p1 = multiprocessing.Process(target=pro1,args=(manager_list,))
    p2 = multiprocessing.Process(target=pro2,args=(manager_list,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
