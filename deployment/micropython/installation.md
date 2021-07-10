
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

last_time = time.time()
while True: nt = time.time(); print('{} {}'.format(adc.read(), nt-last_time)); last_time=nt; time.sleep(1)

adc2 = ADC(Pin(33))

last_time = time.ticks_ms()
while True: nt = time.ticks_us(); print('{:4} {:4} {}'.format(adc.read(), adc2.read(), time.ticks_diff(nt, last_time) - 1000000)); last_time=nt; time.sleep(1)

adc = ADC(Pin(33))
adc = ADC(Pin(34))

valid = []
for i in range(100):
    try:
        print('Pin {}: {}'.format(i+1, ADC(Pin(i+1)).read()))
        valid.append(i+1)
    except:
        print('Failed to read pin {}'.format(i+1))
print(valid)

#[32, 33, 34, 35, 36, 37, 38, 39]
#0, 2, 4, 12, 13, 14, 15, 25, 26, 27, 
#32, 33, 34, 35, 36, 39.

def readall():
    for p in [32, 33, 34, 35, 36, 37, 38, 39]:
        try:
            print('Pin {}: {}'.format(p, ADC(Pin(p)).read()))
        except:
            print('Failed to read pin {}'.format(p))

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






#######MAIN

import machine
import network
# from sht30 import SHT30
import socket
import time
# import tsl2561
import ubinascii
import urequests

MAC = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
print("MAC address: %s" % MAC)

SERVER_IP = '192.168.88.2'
SERVER_PORT = 7266

GLOBAL_CONFIG = {
    'loop_delay': '20',
}


def XX_server_get(path):
    addr = socket.getaddrinfo(SERVER_IP, SERVER_PORT)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, SERVER_IP), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'))
        else:
            break
    s.close()


def _server_get(path):
    response = urequests.get("http://%s:%d/%s" % (SERVER_IP, SERVER_PORT, path))
    print(response.status_code)
    print(response.text)
    try:
        j = response.json()
    except Exception as e:
        print(str(e))
        return
    for k in j.keys():
        print("%s : %s" % (k, j[k]))
        if k == 'MACHINE_RESET':
            if j[k] == MAC:
                print("Rebooting on request!")
                machine.reset()
            else:
                print("MAC address DID NOT MATCH, not rebooting!")
        if k == 'TERMINATE_SCRIPT':
            if j[k] == MAC:
                print("Terminating python script!")
                raise Exception
            else:
                print("MAC address DID NOT MATCH, not terminating!")
        GLOBAL_CONFIG[k] = j[k]


def _send_sensor(sensor_type, info_dict):
    path = "upload_data/%s?mac_address=%s" % (sensor_type, MAC)
    for k in info_dict.keys():
        path = path + "&%s=%s" % (k, info_dict[k])
    _server_get(path)


def send_tsl2561(level):
    _send_sensor('tsl2561',
                 {'light_level': str(level)})


def send_sht30(temperature, humidity):
    _send_sensor('sht30',
                 {'temperature': str(temperature),
                  'humidity': str(humidity)})


def main_loop():
    return
    i2c = machine.I2C(-1, scl=machine.Pin(5), sda=machine.Pin(4))
    sens = tsl2561.TSL2561(i2c)
    sens_sht = SHT30()
    while True:
        level = sens.read()
        print(level)
        send_tsl2561(level)
        temperature, humidity = sens_sht.measure()
        print('Temperature:', temperature, 'C, RH:', humidity, '%')
        send_sht30(temperature, humidity)
        time.sleep(float(GLOBAL_CONFIG['loop_delay']))


def setup_network():
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Raccoon', 'grindelwald123')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    ap_if.active(False)

def halt_network():
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(False)
    ap_if.active(False)

setup_network()
# main_loop()
# halt_network()
# print('NOT starting up WiFi, want to reduce power consumption!')

led = machine.Pin(16, machine.Pin.OUT)
for i in range(10):
    led.value(0)
    time.sleep(0.01)
    led.value(1)
    time.sleep(0.1)        
led.value(1)
print('Waiting 4 seconds...')
time.sleep(4)
print('Shutting down for 5 minutes.')
machine.deepsleep(5 * 60000)

#######

from icmplib import ping
import time

def p():
    while True:
        h = ping('192.168.88.178',privileged=False)
        print((h.packet_loss, h.packets_sent, h.packets_received, h.is_alive))
        if h.packets_received > 0:
            print(f'{time.asctime()}\x07')

