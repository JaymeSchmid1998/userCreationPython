from pathlib import *
import time
import RPi.GPIO as GPIO
import nfc
import ndef
import threading
import nfc.snep
import time
# coding: utf-8
def CreateUserId():
    
    my_file=Path('UserCreation.txt')
    mylines = []
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22,GPIO.OUT)
    GPIO.setup(20,GPIO.OUT)
    GPIO.setup(12,GPIO.OUT)
    # this checks if the file exists
    if my_file.exists():
        clf = nfc.ContactlessFrontend('')
#if it does hthen open it and append the lines to the array
        objText = open('UserCreation.txt', "r")
        for line in objText:
            mylines.append(line)

    
  #  lstLines = objText.readlines()
   # print (lstLines)
        mytext=mylines[0].rstrip('AuthCode:')
        print(mytext)
#this just gets the raw code =, it doesth is by replacing the text auth code with nothing    

        mytext1 = mytext.replace("AuthCode: ", "")

        print(mytext1)
        GPIO.output(22,1)
        GPIO.output(20,0)
        GPIO.output(12,0)
    
        objText.close()
        my_file.unlink()
        print('file found')
        try:
            clf = nfc.ContactlessFrontend('tty:USB0:pn532')
            clf.connect(llcp={})
            def on_connect(llc):
                threading.Thread(target=llc.run).start(); return False
            llc = clf.connect(llcp={'on-connect': on_connect})
            print (llc)
            snep = nfc.snep.SnepClient(llc)
            snep.put_records([ndef.TextRecord(mytext1, "de")])
            GPIO.output(22,0)
            clf.close()
        except: 
            clf.close()
            print('error')
            GPIO.output(12,1)
            GPIO.output(22,0)
            GPIO.output(20,0)
        
    else:
        print('no file found')
        GPIO.output(22,0)
        GPIO.output(12,0)
        GPIO.output(20,1)
RunInf=True
try:
    while RunInf==True:
        CreateUserId()
        time.sleep( 5 )
except:
    print('error')
        