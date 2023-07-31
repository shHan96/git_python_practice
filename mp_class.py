from multiprocessing import Process, freeze_support


# 클래스 선언 부분
class HelloProcess(Process): #Process 클래스 상속
    def __init__(self): # 생성자 메서드
        super(Process,self).__init__() # 슈퍼 클래스의 Process클래스의 생성자 호출
        
        
    def run(self) -> None:
        print("Hello Process2")
        
        
        
#메인 코드 부분

if __name__ == "__main__":
    
    freeze_support() # 윈도우에서의 멀티프로세싱할 때 필요
    p1 = HelloProcess() # 프로세스의 객체 생성
    p1.start()
    p1.join()
    p1.terminate() # 생략가능
    

