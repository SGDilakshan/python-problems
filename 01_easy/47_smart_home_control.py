# Create a Python program using OOP and method overriding where different smart home devices respond differently to a common activate() command.

class Device:
    def activate(self):
        print("Device activated.")

class Light(Device):
    def activate(self):
        print("Light turned ON.")

class Fan(Device):
    def activate(self):
        print("Fan started spinning.")

class DoorLock(Device):
    def activate(self):
        print("Door locked securely.")

devices = [Light(), Fan(), DoorLock()]
for d in devices:
    d.activate()
