buttonslist = []

from logipy import logi_led
import time

def flash_rgb(code):
    r = 100
    g = 0
    b = 0
    for i in range (20):
        logi_led.logi_led_set_lighting_for_key_with_hid_code(code,100,100,100)
        logi_led.logi_led_set_lighting_for_key_with_hid_code(code,r,g,b)
        b +=5
        r -=5
        time.sleep(0.00001)
    for i in range (20):
        logi_led.logi_led_set_lighting_for_key_with_hid_code(code,100,100,100)

        logi_led.logi_led_set_lighting_for_key_with_hid_code(code,r,g,b)
        g +=5
        b -=5
        time.sleep(0.00001)

    for i in range (20):
        logi_led.logi_led_set_lighting_for_key_with_hid_code(code,100,100,100)

        logi_led.logi_led_set_lighting_for_key_with_hid_code(code,r,g,b)
        r +=5
        g -=5
        time.sleep(0.00001)


NAME = 0
CODE = 1
NEAR = 2
MID = 3
DICT_CODE = 0
DICT_NEAR = 1
DICT_MID = 2

logi_led.logi_led_init()
file = open("näppäimet.csv","r")
buttonlines = file.readlines()
buttonsdict= {}


for line in buttonlines:
    data = line.replace("\n","").split(";")
    number, button, close_buttons, mid_buttons = int(data[0]), data[1], data[2].split(","), data[3].split(",")
    buttonslist.append([button,number,close_buttons,mid_buttons])
    buttonsdict[button] = [number,close_buttons,mid_buttons]

time.sleep(1.5)
for led in buttonslist:
    logi_led.logi_led_set_lighting(100, 0, 0)
    logi_led.logi_led_set_lighting_for_key_with_hid_code(int(led[CODE]), 0, 100, 0)
    print(led[NAME])
    for lamp in led[NEAR]:
        flash_rgb(buttonsdict[lamp][DICT_CODE])
    time.sleep(0.01)
time.sleep(5)

