    
class TrafficDevice:
    def __init__(self, device_name):
        # Encapsulation
        self.__device_name = device_name

    def get_device_name(self):
        return self.__device_name

    def activate(self):
        print(f"{self.__device_name} is activated.")


class TrafficLight(TrafficDevice):
    def __init__(self):
        super().__init__("Traffic Light")

    def activate(self):
        print(f"{self.get_device_name()}: Changing lights (Red → Yellow → Green).")


class SpeedCamera(TrafficDevice):
    def __init__(self):
        super().__init__("Speed Camera")

    def activate(self):
        print(f"{self.get_device_name()}: Capturing speeding vehicles.")


class PedestrianSignal(TrafficDevice):
    def __init__(self):
        super().__init__("Pedestrian Signal")

    def activate(self):
        print(f"{self.get_device_name()}: Displaying WALK signal for pedestrians.")
class EmergencySiren(TrafficDevice):
    def __init__(self):
        super().__init__("Emergency Siren")

    def activate(self):
        print(f"{self.get_device_name()}: Sounding emergency alert for priority vehicles.")


traffic_light = TrafficLight()
speed_camera = SpeedCamera()
pedestrian_signal = PedestrianSignal()
emergency_siren = EmergencySiren()

devices = [
    traffic_light,
    speed_camera,
    pedestrian_signal,
    emergency_siren
]

print("Smart Traffic Management System\n")

for device in devices:
    device.activate()
