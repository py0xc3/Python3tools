#!/usr/bin/python3

import os

ch1 = ["ARD HD, ARTE HD", "/opt/bin/mediaclient -m DVBS2 -f 11494000 -M QPSK -S 22000000 -V H -E 2/3"]
ch2 = ["ZDF HD", "/opt/bin/mediaclient -m DVBS2 -f 11362000 -M QPSK -S 22000000 -V H -E 2/3"]
ch3 = ["ZDF, 3SAT, ...", "/opt/bin/mediaclient -m DVBS -f 11954000 -M QPSK -S 27500000 -V H -E 3/4"]
ch4 = ["Servus TV", "/opt/bin/mediaclient -m DVBS2 -f 11303000 -M QPSK -S 22000000 -V H -E 2/3;"]
ch5 = ["VOX, RTL, ...", "/opt/bin/mediaclient -m DVBS -f 12188000 -M QPSK -S 27500000 -V H -E 3/4"]
ch6 = ["RTL nitro", "/opt/bin/mediaclient -m DVBS -f 12663000 -M QPSK -S 22000000 -V H -E 5/6"]
ch7 = ["Pro7, Sat1, K1, ...", "/opt/bin/mediaclient -m DVBS -f 12545000 -M QPSK -S 22000000 -V H -E 5/6"]
ch8 = ["MDR, RBB", "/opt/bin/mediaclient -m DVBS2 -f 10891000 -M QPSK -S 22000000 -V H -E 2/3"]
ch9 = ["ARD ONE", "/opt/bin/mediaclient -m DVBS2 -f 11053000 -M QPSK -S 22000000 -V H -E 2/3"]
ch10 = ["ARD, ...", "/opt/bin/mediaclient -m DVBS -f 11837000 -M QPSK -S 27500000 -V H -E 3/4"]
ch11 = ["BBC HD", "/opt/bin/mediaclient -m DVBS2 -f 11229000 -M QPSK -S 22000000 -V V -E 2/3"]
ch12 = ["CNN", "/opt/bin/mediaclient -m DVBS -f 11627000 -M QPSK -S 22000000 -V V -E 5/6"]
ch13 = ["TELE5", "/opt/bin/mediaclient -m DVBS -f 12480000 -M QPSK -S 27500000 -V V -E 3/4"]

print(" 1)", ch1.pop(0))
chanselection = [ch1.pop(0)]
print(" 2)", ch2.pop(0))
chanselection.append(ch2.pop(0))
print(" 3)", ch3.pop(0))
chanselection.append(ch3.pop(0))
print(" 4)", ch4.pop(0))
chanselection.append(ch4.pop(0))
print(" 5)", ch5.pop(0))
chanselection.append(ch5.pop(0))
print(" 6)", ch6.pop(0))
chanselection.append(ch6.pop(0))
print(" 7)", ch7.pop(0))
chanselection.append(ch7.pop(0))
print(" 8)", ch8.pop(0))
chanselection.append(ch8.pop(0))
print(" 9)", ch9.pop(0))
chanselection.append(ch9.pop(0))
print("10)", ch10.pop(0))
chanselection.append(ch10.pop(0))
print("11)", ch11.pop(0))
chanselection.append(ch11.pop(0))
print("12)", ch12.pop(0))
chanselection.append(ch12.pop(0))
print("13)", ch13.pop(0))
chanselection.append(ch13.pop(0))

print("Choose a channel:")
while 1:
    try:
        chanraw = int(input())
        chanraw = chanraw - 1
        break
    except:
        print("It has to be one of the numbers above!")

chan = chanselection.pop(chanraw)
    
os.system(chan)
os.system("vlc dvb-t://frequency=0000:bandwidth=0 &")
