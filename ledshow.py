from logipy import logi_led
import time
logi_led.logi_led_init()
time.sleep(1)
file = open("näppäimet.csv","r")
b = file.readlines()
for i in range(len(b)):
    b[i] = b[i].split(";")
while True:
    for i in b:
        logi_led.logi_led_set_lighting(100,0,0)
        logi_led.logi_led_set_lighting_for_key_with_hid_code(int(i[0]),0,100,0)
        logi_led.logi_led_set_lighting_for_key_with_hid_code()
        time.sleep(0.1)
    time.sleep(210)
