import time
from playsound import playsound


tapped_ids = {}

while True:
    # check if time is 0:00
    current_time = time.localtime()
    if current_time.tm_hour == 0 and current_time.tm_min == 0:
        tapped_ids.clear()
    
    id = str(input("Tap WatCard: "))        
    
    if id not in tapped_ids:
        tapped_ids[id] = 1
    else:
        tapped_ids[id] += 1
    
    if tapped_ids[id] > 2:
        playsound("Portal2-BuzzerSound.mp3")
        print(tapped_ids[id])
    else:
        playsound("Portal2-Beep.mp3")
    
    time.sleep(1)
