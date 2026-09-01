
from abc import (
    ABC, abstractmethod
)

class Device(ABC):

    @abstractmethod
    def getDeviceName(self):
        pass
    
    @abstractmethod
    def setDeviceOn(self):
        pass
    
    @abstractmethod
    def setDeviceOff(self):
        pass
    
    @abstractmethod
    def setVolume(self):
        pass


class TV(Device):

    def __init__(self):
        self.is_device_on = False
        self.volume_number = 0

    def getDeviceName(self):
        return "TV"
    
    def setDeviceOn(self):
        if self.is_device_on == False:
            print(f"TV device is ON")
            self.is_device_on = True
        else:
            print(f"TV device is already ON")
    
    def setDeviceOff(self):
        if self.is_device_on == True:
            print(f"TV device is OFF")
            self.is_device_on = False
        else:
            print(f"TV device is already OFF")

    def setVolume(self, volume_number):
        if (self.volume_number + volume_number)<0:
            print(f"TV device volume is already low and current volume: {self.volume_number}")
        else:
            self.volume_number = self.volume_number + volume_number


class Radio(Device):

    def __init__(self):
        self.is_device_on = False
        self.volume_number = 0

    def getDeviceName(self):
        return "Radio"
    
    def setDeviceOn(self):
        if self.is_device_on == False:
            print(f"Radio device is ON")
            self.is_device_on = True
        else:
            print(f"Radio device is already ON")
    
    def setDeviceOff(self):
        if self.is_device_on == True:
            print(f"Radio device is OFF")
            self.is_device_on = False
        else:
            print(f"Radio device is already OFF")

    def setVolume(self, volume_number):
        if (self.volume_number + volume_number)<0:
            print(f"Radio device volume is already low and current volume: {self.volume_number}")
        else:
            self.volume_number = self.volume_number + volume_number


class BasicRemoteControl:

    def __init__(self, device_class_obj: Device):
        self.device_class_obj = device_class_obj

    def report(self):
        print(f"Current device: {self.device_class_obj.getDeviceName()}, state: {self.device_class_obj.is_device_on}, volume: {self.device_class_obj.volume_number}")

    def togglePower(self):
        print("Toggle power button is pressed")
        if self.device_class_obj.is_device_on == True:
            self.device_class_obj.setDeviceOff()
        else:
            self.device_class_obj.setDeviceOn()
        self.report()

    def volumeUp(self):
        print("VolumeUp button is pressed")
        self.device_class_obj.setVolume(10)
        self.report()

    def volumeDown(self):
        print("VolumeDown button is pressed")
        self.device_class_obj.setVolume(-10)
        self.report()


class AdvanceRemoteControl(BasicRemoteControl):

    last_volume_number = 0

    def mute_volume(self):
        self.last_volume_number = self.device_class_obj.volume_number
        self.device_class_obj.setVolume(0)
        print(f"Mute volume button is pressed and stored-last-volume-number: {self.last_volume_number}")

    def unmute_volume(self):
        self.device_class_obj.setVolume(self.last_volume_number)
        print(f"Unmute volume button is pressed and restored-volume-number with: {self.last_volume_number}")


def main():

    print("\n")
    tv_class_obj = TV()
    print(f"Printing details about basic remote tv:")
    basic_remote_control_class_obj = BasicRemoteControl(tv_class_obj)
    basic_remote_control_class_obj.report()
    basic_remote_control_class_obj.togglePower()
    basic_remote_control_class_obj.volumeUp()
    basic_remote_control_class_obj.volumeDown()
    basic_remote_control_class_obj.togglePower()


    print("\n")
    tv_class_obj = TV()
    print(f"Printing details about advanced remote tv:")
    advance_remote_control_class_obj = AdvanceRemoteControl(tv_class_obj)
    advance_remote_control_class_obj.report()
    advance_remote_control_class_obj.togglePower()
    advance_remote_control_class_obj.volumeUp()
    advance_remote_control_class_obj.volumeUp()
    advance_remote_control_class_obj.mute_volume()
    advance_remote_control_class_obj.unmute_volume()
    advance_remote_control_class_obj.togglePower()




main()