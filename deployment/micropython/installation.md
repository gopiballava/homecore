
pip3 install esptool

https://micropython.org/download/esp32/

https://micropython.org/resources/firmware/esp32spiram-idf3-20200902-v1.13.bin

esptool.py --chip esp32 --port /dev/cu.usbserial-0001 erase_flash

esptool.py --chip esp32 --port /dev/cu.usbserial-0001 --baud 460800 write_flash -z 0x1000 esp32spiram-idf3-20200902-v1.13.bin


import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()                             # Scan for available access points
sta_if.connect("Puppies", "b33pb33p") # Connect to an AP

sta_if.isconnected()                      # Check for successful connection