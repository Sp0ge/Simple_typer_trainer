import keyboard
import time
import random

run = False
text =""
error = 0

c = input("en or ru ? > ")
if c == "ru":
    lang = "russian.txt"
else:
    lang = "english.txt"
print("Press ENTER to start.")
while True:        
    if keyboard.is_pressed('Enter'):
        with open(lang) as file:
            text = text + str(random.sample(list(file), 2)).replace("[","").replace("]","").replace(",","").replace("'","").replace("\\n","")
            file.close()
        print('   ',text,'   ')
        run = True
    if run:
        startTime = time.time()
        out = input(">>  " )
        endTime = time.time()
        if len(text.strip().replace(" ","")) != 0:
            timeres = endTime - startTime
            speed =  timeres / len(text.strip().replace(" ",""))
        if keyboard.is_pressed('Enter'):
            run = False
            if out.strip() == text.strip():
                print("Good", "( print time = ",timeres,"speed = ",speed,')')
            else:
                print("Bad", timeres)
            
    text = ''
    out = ''
    
