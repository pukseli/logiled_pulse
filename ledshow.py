from logipy import logi_led
import time
time.sleep(1)  # Give the SDK a second to initialize
logi_led.logi_led_init()
r = 100
g = 0
b = 0
file = open("näppäimet_map.csv","w")
while True:
    for i in range (0,120):
        logi_led.logi_led_set_lighting(100,0,0)
        logi_led.logi_led_set_lighting_for_key_with_hid_code(i,0,100,0)
        a = input(str(i) + ": ")
        file.write(str(i) +":" + a)

    break
