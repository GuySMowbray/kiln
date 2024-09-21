# adt7320.py
"""
Class to manage the ADT7320 Temperature Sensor.
This file contains the ADT7320 class, which handles communication with the ADT7320
temperature sensor via SPI to read temperature data.
"""
from machine import Pin, SPI

class ADT7320:
    """
    Class to interact with the ADT7320 temperature sensor via SPI.
        The ADT7320 is a high-accuracy digital temperature sensor that communicates via SPI.
    """
    REG_TEMP = 0x00   # Temperature register address (16-bit data)
    CMD_READ = 0x40   # Read command

    def __init__(self, spi: SPI, cs_pin: Pin):
        """
        Initialize the ADT7320 class with SPI communication and Chip Select (CS) pin.
        :param spi: The SPI interface
        :param cs_pin: The Chip Select pin
        """
        self.spi = spi  # SPI interface
        self.cs = cs_pin  # Chip Select pin for ADT7320
        self.cs.init(Pin.OUT, value=1)  # Set CS pin high (inactive)
      
    def read_temperature(self) -> float:
        """
        Read the temperature from the ADT7320.
        
        This function reads the temperature data from the sensor and converts it to Celsius.
        :return: Temperature in Celsius
        """
        self.cs.value(0)  # Activate Chip Select for ADT7320
        self.spi.write(bytearray([self.CMD_READ | self.REG_TEMP]))  # Send read command for the temperature register
        temp_data = self.spi.read(2)  # Read 2 bytes of temperature data
        self.cs.value(1)  # Deactivate Chip Select

        # Combine the two bytes and convert to temperature (16-bit resolution)
        raw_temp = (temp_data[0] << 8) | temp_data[1]
        
        # Convert raw data to temperature in Celsius
        if raw_temp & 0x8000:  # Negative temperature check (two's complement)
            raw_temp -= 65536
        temperature = raw_temp / 128.0  # 0.0078125°C per LSB

        print(f"ADT7320 Temperature: {temperature:.2f} °C")
        return temperature
