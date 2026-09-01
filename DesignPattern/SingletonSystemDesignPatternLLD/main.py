
import time
import threading

class Singleton:
    
    _instances =  None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instances is None:
            print(f"{threading.current_thread().name} is entered")
            time.sleep(1)
            with cls._lock:
                if cls._instances is None:
                    cls._instances = super().__new__(cls)
                    print(f"{threading.current_thread().name} created object")
                else:
                    print(f"{threading.current_thread().name} reused created object")
        return cls._instances
    
     
def initializeClassConstructor():
    s = Singleton()
    print(f"singleton-class-object-id-memory:{id(s)}")

all_threads = []
for i in range(1, 6):
    t = threading.Thread(target=initializeClassConstructor, name=f"Thread{i}")
    all_threads.append(t)
for t in all_threads:
    t.start()
for t in all_threads:
    t.join()
    

