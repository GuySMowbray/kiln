# device_manager.py
"""
DeviceManager class to manage multiple devices connected to the Raspberry Pi Pico W.
This file contains the DeviceManager class, which initializes and manages multiple devices
such as the AD7193 ADC, AD5201 digital potentiometer, and ADT7320 temperature sensor. It provides
methods to initialize devices, read from them, and control relays.
"""

from ad7193 import AD7193
from ad5201 import AD5201
from adt7320 import ADT7320
from utils import init_spi, init_i2c, control_relays, indicator_led_blink, init_wifi
import config

class DeviceManager:
    """
    Manages all device instances and interactions in the system.
    """
    def __init__(self):
        # Initialize SPI and I2C
        self.spi = init_spi()
        self.i2c = init_i2c()

        # Initialize devices
        self.ad7193 = AD7193(self.spi, config.AD7193_CS_PIN)
        self.ad5201 = AD5201(self.spi, config.AD5201_CS_PIN)
        self.adt7320 = ADT7320(self.spi, config.ADT7320_CS_PIN)

    def initialize_devices(self, reference_value=128):
        """
        Initialize all connected devices.
        :param reference_value: Reference voltage to set on the AD5201 digital potentiometer.
        """
        self.ad7193.init()  # Initialize the AD7193 ADC
        self.ad5201.set_value(reference_value)  # Set reference voltage
        print("Devices initialized.")

    def read_thermocouples(self):
        """
        Read data from all configured thermocouple channels.
        """
        for config_value in [config.AD7193_CONFIG_CH1_2, config.AD7193_CONFIG_CH3_4, config.AD7193_CONFIG_CH5_6]:
            self.ad7193.select_channel_pair(config_value)
            ad7193_data = self.ad7193.read_data()
            print(f"Thermocouple Channel Data: {ad7193_data}")
            time.sleep(1)  # Allow some time between reads
            
    def read_temperature(self):
        """
        Read the temperature from the ADT7320 sensor.
        """
        temperature = self.adt7320.read_temperature()  # Read and print temperature
        return temperature

    def control_relays(self, relay_states):
        """
        Control the states of relays connected to the GPIO pins.
        :param relay_states: A list of states for each relay (1 for ON, 0 for OFF)
        """
        control_relays(relay_states)

