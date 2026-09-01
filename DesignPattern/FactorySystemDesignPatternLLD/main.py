
from abc import (
    ABC, 
    abstractmethod
)

# ---------- Product ----------
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# ---------- Concrete Product ----------
class Truck(Transport):
    def deliver(self):
        print(f"Delivering by truck")

class Ship(Transport):
    def deliver(self):
        print(f"Delivering by ship")


# ---------- Creator ----------
class Logistics(ABC):

    # Factory Method
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    # Creator's real work
    def planDelivery(self):
        transport_class_obj = self.create_transport()
        transport_class_obj.deliver()


# ---------- Concrete Creators ----------

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()



def main():
    logistics = RoadLogistics()
    logistics.planDelivery()
    logistics = SeaLogistics()
    logistics.planDelivery()

main()


