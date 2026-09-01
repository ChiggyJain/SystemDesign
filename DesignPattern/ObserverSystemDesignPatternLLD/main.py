
from abc import ABC

class Observer(ABC):
    def update(self, msg):
        pass

class PhoneObserver(Observer):
    def update(self, msg):
        print(f"Notifying Phone-Observer-Class: {self.__class__.__name__}, ObjectID: {id(self)}, Msg: {msg}")

class DesktopObserver(Observer):
    def update(self, msg):
        print(f"Notifying Desktop-Observer-Class: {self.__class__.__name__}, ObjectID: {id(self)}, Msg: {msg}")

class WeatherStation:

    def __init__(self):
        self.msg = ""
        self.subscriber_list = []

    def subscribe(self, observer_class_obj: Observer):
        self.subscriber_list.append(observer_class_obj)

    def unsubscribe(self, observer_class_obj: Observer):
        self.subscriber_list.remove(observer_class_obj)

    def set_measurement(self, msg):
        self.msg = msg

    def notifyAll(self):
        print("============================================================================================================")
        print(f"Weather station, will be notifying latest messages to {len(self.subscriber_list)} observer/subscriber asap")
        for each_observer_class_obj in self.subscriber_list:
            each_observer_class_obj.update(self.msg)
        print("============================================================================================================")



def main():

    observer_class_obj1 = PhoneObserver()
    observer_class_obj2 = PhoneObserver()
    observer_class_obj3 = DesktopObserver()
    weather_station_class_obj = WeatherStation()
    weather_station_class_obj.subscribe(observer_class_obj1)
    weather_station_class_obj.subscribe(observer_class_obj2)
    weather_station_class_obj.subscribe(observer_class_obj3)
    weather_station_class_obj.set_measurement("Today heavy rainfall within 5minutes")
    weather_station_class_obj.notifyAll()
    weather_station_class_obj.unsubscribe(observer_class_obj2)
    weather_station_class_obj.set_measurement("Heavy storm within 5minutes")
    weather_station_class_obj.notifyAll()

main()