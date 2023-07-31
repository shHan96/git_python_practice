class Car:
    color = "" # 인스턴스 변수
    speed = 0  # 인스턴스변수
    
    def __init__(self,value1,value2): # 두개의 매개변수
        self.cont = self
        print(f'self 매개변수의 값: {self.cont}')  
        self.color = value1 
        print(f"color변수의 메모리 위치: {hex(id(self.color))}")
        self.speed = value2
        print(f"speed변수의 메모리 위치: {(id(self.speed)):0X}")

    def __repr__(self) -> str:
        return "Hello"
    
    def upSpeed(self,value):
        self.speed +=value
    def downSpeed(self, value):
        self.speed -=value


c1 = Car("빨강",30)
print(f'myCar1의 내용:{c1}')