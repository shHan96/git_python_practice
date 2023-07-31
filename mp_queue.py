##### 프로세스 간의 객체 공유: Queue() #########
# 큐의 특징 : 데이터가 몇개 남았는지 카운터가 동작함.


# from multiprocessing import Queue, Process
# import time
# def pro1(q):
#     # q 객체에 데이터를 넣는다.
#     for i in range(100):
#         q.put(i) # 데이터를 입혁하는 메소드

# def pro2(q):
#     items = []
#     while not q.empty(): # 무한 루프
#         time.sleep(0.1)
#         item=q.get() # q에 있는 데이터를 가지고옴
#         items.append(item)
#         print(f"p2: q객체에서 {item}를 가져왔습니다")
#         print(f"현재 q에 저장된 값은 {items} 입니다")
        

# if __name__ == "__main__":
#     queue = Queue() # 데이터를 공유할 큐객체 생성
#     p1 = Process(target=pro1,args=(queue,))
#     p2 = Process(target=pro2,args=(queue,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

###################################### 위의 프로그램이 종료되도록 수정하겠습니다.######################


# from multiprocessing import Queue, Process
# import time
# def pro1(q):
#     # q 객체에 데이터를 넣는다.
#     for i in range(100):
#         q.put(i) # 데이터를 입혁하는 메소드
#         time.sleep(0.1)


# def pro2(q):
#     items = []
#     while True: # 무한 루프
#         item=q.get(timeout=1) # q에 있는 데이터를 가지고옴
#         if item is None:
#             print("모든 데이터를 가지고 왔습니다.")
#             break
#         items.append(item)
#         print(f"p2: q객체에서 {item}를 가져왔습니다")
#         print(f"현재 q에 저장된 값은 {items} 입니다")
        

# if __name__ == "__main__":
#     queue = Queue() # 데이터를 공유할 큐객체 생성
#     p1 = Process(target=pro1,args=(queue,))
#     p2 = Process(target=pro2,args=(queue,))
#     p1.start()
#     p2.start()
    
#     p1.join()
#     queue.put(None)
#     p2.join()
#     p1.terminate()
#     p2.terminate()

## 설명: 프로세스 간 통신을 위해 multiprocessing. Queue
    