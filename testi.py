buttonslist = []

from logipy import logi_led
import time
import random
from multiprocessing import Process


def flash_rgb():
    r = 100
    g = 0
    b = 0
    code =  random.randint(4,100)
    for i in range (20):
        logi_led.logi_led_set_lighting_for_key_with_hid_code(code,100,100,100)
        logi_led.logi_led_set_lighting_for_key_with_hid_code(code,r,g,b)
        b +=5
        r -=5
        time.sleep(0.01)
    for i in range (20):
        logi_led.logi_led_set_lighting_for_key_with_hid_code(code,100,100,100)

        logi_led.logi_led_set_lighting_for_key_with_hid_code(code,r,g,b)
        g +=5
        b -=5
        time.sleep(0.01)

    for i in range (20):
        logi_led.logi_led_set_lighting_for_key_with_hid_code(code,100,100,100)

        logi_led.logi_led_set_lighting_for_key_with_hid_code(code,r,g,b)
        r +=5
        g -=5
        time.sleep(0.01)


if __name__ == "__main__":
    logi_led.logi_led_init()
    file = open("näppäimet.csv","r")
    buttonlines = file.readlines()
    buttonsdict= {}
    buttonslist = []

    for line in buttonlines:
        data = line.replace("\n","").split(";")
        number, button, close_buttons, mid_buttons = int(data[0]), data[1], data[2].split(","), data[3].split(",")
        buttonslist.append([button,number,close_buttons,mid_buttons])
        buttonsdict[button] = [number,close_buttons,mid_buttons]

    logi_led.logi_led_init()
    time.sleep(1)
    while True:
        logi_led.logi_led_set_lighting_for_key_with_hid_code(buttonslist[random.randint(0,len(buttonslist))][1], random.randint(0,100), random.randint(0,100), random.randint(0,100))
        time.sleep(0.002)
