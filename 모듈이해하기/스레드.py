
import threading
import time


class Worker(threading.Thread): # 상속
    def __init__(self, name):
        super().__init__()
        self.name = name # 생성자에서 thread 이름 지정

    def run(self): # 스레드가 실행될 때 호출되는 메소드
        print("sub thread start ", threading.currentThread().getName())
        time.sleep(3) # 3초 대기
        print("sub thread end ", threading.currentThread().getName())


print("main thread start")
for i in range(5):
    name = "thread {}".format(i)
    t = Worker(name) # 서브스레드 5개 생성 -> 독립적으로 동작
    t.start() # sub thread의 run 메서드를 호출 - 각각 3초 대기 후 종료메시지를 출력한다. -> 그래서 종료 스레드 순서가 매번 바뀜

print("main thread end") # 모든 서브 스레드가 시작되면 메인 스레드 종료메시지를 출력한다.