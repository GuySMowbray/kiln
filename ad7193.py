# ad7193.py
"""
Class to manage the AD7193 Analog-to-Digital Converter (ADC).
This file contains the AD7193 class, which handles communication with the AD7193 ADC
via SPI to perform high-resolution analog-to-digital conversions for multiple differential
input channels.
"""

from machine import Pin, SPI
import time

class AD7193:
    """
    Class to interact with the AD7193 ADC via SPI.
    The AD7193 is a high-resolution ADC that can be configured to read multiple differential
    inputs (pairs of channels) and convert analog signals to digital values.
    """
    REG_STATUS = 0x00   # Status Register
    REG_MODE = 0x01     # Mode Register
    REG_CONFIG = 0x02   # Configuration Register
    REG_DATA = 0x03     # Data Register (where the converted data is read from)
    REG_GPOCON = 0x05   # General-purpose I/O Configuration Register
    MODE_CONT = 0x060000  # Continuous Conversion Mode - the ADC keeps sampling continuously
  
    def __init__(self, spi: SPI, cs_pin: Pin):
        """
        Initialize the AD7193 class with SPI communication and Chip Select (CS) pin.
        :param spi: The SPI interface
        :param cs_pin: The Chip Select pin
        """
        self.spi = spi  # SPI interface
        self.cs = cs_pin  # Chip Select pin for AD7193
        self.cs.init(Pin.OUT, value=1)  # Set CS pin high (inactive)

    def write_register(self, register: int, value: int) -> None:
        """
        Write a value to a specific AD7193 register.
        :param register: The register address to write to
        :param value: The 24-bit value to write
        """
        self.cs.value(0)  # Activate CS (chip select is active low)
        # Send the register address with the write bit (0) and the value to be sent
        self.spi.write(bytearray([0x10 | (register << 3), (value >> 16) & 0xFF, (value >> 8) & 0xFF, value & 0xFF]))
        self.cs.value(1)  # Deactivate CS

    def read_register(self, register: int, num_bytes: int) -> bytes:
        """
        Read a value from a specific AD7193 register.
        :param register: The register address to read from
        :param num_bytes: The number of bytes to read
        :return: The data read from the register
        """
        self.cs.value(0)  # Activate CS
        self.spi.write(bytearray([0x38 | (register << 3)]))  # Read command for register
        result = self.spi.read(num_bytes)  # Read the specified number of bytes
        self.cs.value(1)  # Deactivate CS
        return result

    def init(self) -> None:
        """
        Initialize the AD7193 ADC.
        This function sets the AD7193 to continuous conversion mode, allowing it to keep sampling data.
        """
        self.write_register(self.REG_MODE, self.MODE_CONT)  # Set Continuous Conversion Mode
        print("AD7193 initialized in Continuous Conversion Mode.")

    def select_channel_pair(self, config: int) -> None:
        """
        Select a specific differential channel pair (e.g., 1-2, 3-4, 5-6).
        :param config: Configuration value for the channel pair
        """
        self.write_register(self.REG_CONFIG, config)
        print(f"AD7193 channel pair set with config: 0x{config:06X}")

    def read_data(self) -> int:
        """
        Read conversion data from the AD7193 ADC.
        :return: 24-bit ADC conversion result
        """
        data = self.read_register(self.REG_DATA, 3)
        result = (data[0] << 16) | (data[1] << 8) | data[2]
        print(f"AD7193 Data: {result}")
        return result

