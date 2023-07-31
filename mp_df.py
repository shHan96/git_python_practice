from multiprocessing import Process, freeze_support

def Hello():
    print("Hello Process")
    
#메인 코드 함수 호출

if __name__=='__main__': #스크립트의 진입점.
    # 현재 스크립트가 직접 실행되는 경우에만 코드블럭을 실행을 보장한다.
    # 다른 스크립트에서(.py) 임포트하면 실행이 안된다.
    freeze_support() # 윈도우에서 멀티 프로세싱을 사용할 때 필요한 함수를 호출함
    
    # 프로세스 생성
    p1 = Process(target=Hello) #Hello 메서드를 실행할 프로세스가 객체가 생성
    p1.start() # 프로세스 시작
    p1.join() # 프로세스 종료시까지 대기하는 메소드
    p1.terminate()