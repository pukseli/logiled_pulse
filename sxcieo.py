keys = " 4: a;;6: c;;7: d;;8: e;;10: g;;11: h;;12: i;;13: j;;15: l;;16: m;;17: n;;18: o;;19: p;;20: q;;21: r;;22: s;;23: t;;24: u;;25: v;;27: x;;28: y;;30: 1;;31: 2;;32: 3;;33: 4;;35: 6;;37: 8;;38: 9;;39: 0;;40: entr;;41: esc;;42: backspace;;43: tab;;44: space;;46: ´;;47: å;;48: ¨;;49: ohi;;50: ';;51: ö;;52: ä;;54: ,;;55: .;;56: -;;57: caps;;58: f1;;59: f2;;61: f4;;62: f5;;64: f7;;65: f8;;66: f9;;67: f10;;68: f11;;69: f12;;70: prinyprintscreen;;71: scroll_lock;;72: pause;;73: insert;;74: home;;75: page_up;;76: delete;;77: end;;78: pagedown;;79: arrow_right;;80: arrow_left;;81: arrow_down;;82: arrow_up;;83: num_numlock;;84: num_/;;85: num_*;;86: num_-;;87: num_+;;88: num_enter;;89: num_1;;90: num_2;;91: num_3;;92: num_4;;93: num_5;;94: num_6;;95: num_7;;96: num_8;;97: num_9;;98: num_0;;100: <;;101: optionsmenu;;224: left_cntrl;;225: lfet_shift;;227: left_window;;228: rigt_cntrl;;229: rigth_shift;;230: alt_cntl ;;231: rigth_window"

while True:
    if " " in  keys:
        keys = keys.replace(" ", "")
    else:
        break

while ":" in keys:
    keys = keys.replace(":",";")
a = keys.split(";;")
file = open("näppäimet_map.csv", "w")
for i in range(len(a)):
    file.write(a[i] + "\n")
file.close()

