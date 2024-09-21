# main_controller.py
"""
MainController class to handle the main loop and application logic.

This file contains the MainController class, which orchestrates the initialization, device management,
and main application loop for the Raspberry Pi Pico W project.
"""

from device_manager import DeviceManager
from utils import indicator_led_blink, init_wifi
import time

class MainController:
    """
    Controls the main loop and application logic.
    """
    def __init__(self):
        self.device_manager = DeviceManager()

    def run(self):
        # Initialize devices and Wi-Fi
        self.device_manager.initialize_devices(reference_value=128)
        init_wifi()

        print("System setup complete. Entering main loop...")
        while True:
            # Blink the LED to indicate the system is running and healthy
            indicator_led_blink()

            # Read thermocouple data
            self.device_manager.read_thermocouples()

            # Read temperature data
            temperature = self.device_manager.read_temperature()
            print(f"ADT7320 Temperature: {temperature:.2f} °C")

            # Control relays to demonstrate their usage
            self.device_manager.control_relays([1, 0, 1])
            time.sleep(2)
            self.device_manager.control_relays([0, 1, 0])
            time.sleep(2)

# Run the main controller if this script is executed
if __name__ == "__main__":
    controller = MainController()
    controller.run()
