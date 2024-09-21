#utils

from machine import I2C, SPI, Pin
import time
import network
import config

def init_spi() -> SPI:
    """
    Initialize the SPI interface for the connected devices.
    :return: Configured SPI object
    """
    spi = SPI(0, baudrate=config.SPI_BAUDRATE, polarity=config.SPI_POLARITY, phase=config.SPI_PHASE, sck=config.SPI_SCK_PIN, mosi=config.SPI_MOSI_PIN, miso=config.SPI_MISO_PIN)
    config.AD7193_CS_PIN.value(1)  # Set CS pin high (inactive)
    config.ADT7320_CS_PIN.value(1)  # Set CS pin high (inactive)
    print("SPI devices initialized.")
    return spi

def init_i2c() -> I2C:
    """
    Initialize the I2C interface and scan for connected devices.
    :return: Configured I2C object
    """
    i2c = I2C(0, scl=config.I2C_SCL_PIN, sda=config.I2C_SDA_PIN, freq=config.I2C_FREQUENCY)
    devices = i2c.scan()
    if devices:
        print("I2C devices found:", [hex(device) for device in devices])
    else:
        print("No I2C devices found.")
        
    # Initialize MCP4725 DAC
    if config.MCP4725_ADDR in devices:
        i2c.writeto(config.MCP4725_ADDR, b'\x40\x80\x00')  # Set DAC output to mid-scale
        print("MCP4725 DAC initialized.")
    return i2c

def control_relays(relay_states: list[int]) -> None:
    """
    Control the states of the relays connected to GPIO pins.
    :param relay_states: A list of states for each relay (1 for ON, 0 for OFF)
    """
    for relay, state in zip(config.RELAY_PINS, relay_states):
        relay.value(state)
    print(f"Relays set to states: {relay_states}")

def indicator_led_blink() -> None:
    """
    Blink the onboard LED to indicate system health or activity.
    """
    config.LED_PIN.toggle()
    time.sleep(0.5)
    
def init_wifi() -> None:
    """
    Initialize the Wi-Fi module on the Pico W.
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print("Wi-Fi initialized. Ready for configuration.")
    # Uncomment the following lines to connect to a network
    # wlan.connect('SSID', 'password')
    # while not wlan.isconnected():
    #     time.sleep(1)
    # print("Connected to Wi-Fi:", wlan.ifconfig())
