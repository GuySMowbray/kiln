# config.py
"""
Configuration settings  Raspberry Pi Pico W for this trial
This file contains all the configuration constants, pin assignments, and settings
used throughout the project for SPI, I2C, GPIO, and device-specific configurations.
"""
import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
from machine import Pin

# SPI Configuration
SPI_BAUDRATE = 1_000_000  # Baud rate for SPI communication
SPI_POLARITY = 0          # SPI polarity
SPI_PHASE = 0             # SPI phase

# SPI Communication Pins
SPI_SCK_PIN = Pin(18)     # SPI Clock pin
SPI_MOSI_PIN = Pin(19)    # Master Out Slave In pin
SPI_MISO_PIN = Pin(16)    # Master In Slave Out pin# Relay Configuration
RELAY_PINS = [Pin(7, Pin.OUT), Pin(8, Pin.OUT), Pin(9, Pin.OUT)]  # GPIO pins for relay control

# Chip Select Pins for SPI Devices
AD7193_CS_PIN = Pin(12, Pin.OUT)  # Chip Select pin for AD7193 ADC
AD5201_CS_PIN = Pin(12, Pin.OUT)  # Chip Select pin for AD5201 Potentiometer (same pin via DOUT)
ADT7320_CS_PIN = Pin(17, Pin.OUT)  # Chip Select pin for ADT7320 Cold Junction Temperature Sensor

# I2C Configuration
I2C_SDA_PIN = Pin(4)  # I2C Data pin
I2C_SCL_PIN = Pin(5)  # I2C Clock pin
I2C_FREQUENCY = 100_000  # Frequency for I2C communication

# MCP4725 DAC Configuration
MCP4725_ADDR = 0x62  # I2C address for the MCP4725 DAC for Analogue heater
# Navkey Configuration
NAVKEY_ADDR = 0x10  # I2C address for the NAVKEY Joypad
# LCD Configuration
I2CLCD_ADDR = 0x27 # I2C address for the LCD display

# Relay Configuration
RELAY_PINS = [Pin(7, Pin.OUT), Pin(8, Pin.OUT), Pin(9, Pin.OUT)]  # GPIO pins for relay control for on/off heaters

# LED Configuration
LED_PIN = Pin(0, Pin.OUT)  # Onboard LED pin (WL_GPIO0 on the Pico W) used as a running indicator 

# AD7193 Configuration
AD7193_CONFIG_CH1_2 = 0x80013B  # Configuration for Channel 1-2 with Gain 8 thermocouple 1
AD7193_CONFIG_CH3_4 = 0x80023B  # Configuration for Channel 3-4 with Gain 8 thermocouple 2
AD7193_CONFIG_CH5_6 = 0x80043B  # Configuration for Channel 5-6 with Gain 8 thermocouple 3

# end
