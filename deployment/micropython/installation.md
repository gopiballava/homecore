
pip3 install esptool

https://micropython.org/download/esp32/

https://micropython.org/resources/firmware/esp32spiram-idf3-20200902-v1.13.bin

esptool.py --chip esp32 --port /dev/cu.usbserial-0001 erase_flash

esptool.py --chip esp32 --port /dev/cu.usbserial-0001 --baud 460800 write_flash -z 0x1000 esp32spiram-idf3-20200902-v1.13.bin


import webrepl_setup

# Interesting Python stuff

import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan()                             # Scan for available access points
sta_if.connect('Raccoon', 'grindelwald123')
sta_if.connect("Puppies", "b33pb33p") # Connect to an AP

sta_if.isconnected()                      # Check for successful connection

sta_if.ifconfig()

import esp32
import time
while True: print(esp32.hall_sensor())


from machine import ADC, Pin

adc = ADC(Pin(32))          # create ADC object on ADC pin

adc.read()                  # read value, 0-4095 across voltage range 0.0v - 1.0v
while True: print(adc.read()); time.sleep(1)

for i in range(35):
   print(ADC(Pin(i+1)).read())

adc.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
adc.width(ADC.WIDTH_9BIT)   # set 9 bit return values (returned range 0-511)
adc.read()                  # read value using the newly configured attenuation and width


import time

from machine import Pin

pin_list = [16, 5, 4, 0]

Pin_list = [Pin(x, Pin.OUT) for x in pin_list]


def is_on(step, j):
    half_step = int(step/2)
    if  j == half_step:
        return True
    if step % 2 == 0:
        return False
    j = (j - 1) % 4
    return j == half_step

def ton(x):
    print(is_on(x, 0), is_on(x, 1), is_on(x, 2), is_on(x, 3))    



def up(r=100, d=0.01):
    for x in range(r):
        for i in range(8):
            for j in range(4):
                if is_on(i, j):
                    Pin_list[j].on()
                else:
                    Pin_list[j].off()
                time.sleep(d)
    for j in range(4):
        Pin_list[j].off()


def up(r=10, d=0.01):
    for x in range(r):
        for i in range(4):
            for j in range(4):
                if i == j:
                    Pin_list[j].on()
                else:
                    Pin_list[j].off()
                time.sleep(d)


def down(r=10, d=0.01):
    for x in range(r):
        for i in range(4):
            for j in range(4):
                if i == j:
                    Pin_list[3-j].on()
                else:
                    Pin_list[3-j].off()
                time.sleep(d)


