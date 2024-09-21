# ad5201.py
"""
Class to manage the AD5201 Digital Potentiometer.
This file contains the AD5201 class, which handles communication with the AD5201
digital potentiometer via SPI to set the reference voltage for the ADC.
"""

from machine import Pin, SPI

class AD5201:
    """
    Class to interact with the AD5201 digital potentiometer via SPI.
    The AD5201 is used to adjust the reference voltage for the ADC.
    """
    def __init__(self, spi: SPI, cs_pin: Pin):
     """
    Initialize the AD5201 class with SPI communication and Chip Select (CS) pin.
    :param spi: The SPI interface
    :param cs_pin: The Chip Select pin
     """
       self.spi = spi  # SPI interface
       self.cs = cs_pin  # Chip Select pin for AD5201
       self.cs.init(Pin.OUT, value=1)  # Set CS pin high (inactive)

    def set_value(self, value: int) -> None:
     """
    Set the resistance value of the AD5201 digital potentiometer.
    The resistance value affects the reference voltage used by the ADC.
    :param value: Resistance value (0 to 255)
    """
       value = max(0, min(255, value))  # Ensure value is within the allowed range

       # Write value to AD5201
       self.cs.value(0)  # Activate CS
       self.spi.write(bytearray([value]))  # Send value to the AD5201
       self.cs.value(1)  # Deactivate CS
       print(f"AD5201 value set to {value}.")
