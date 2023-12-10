import time
from datetime import date
from playsound import playsound
 
 
cleared_day = str(date.today())
tapped_ids = {}
 
 
def is_valid_id(id):
    if len(id) != 8:
        return False
    for i in id:
        if "0" > i or i > "9":
            return False
    return True
 
 
while True:    
    id = str(input("Tap WatCard: "))
    
    today = str(date.today())
    if today != cleared_day:
        tapped_ids.clear()
        cleared_day = today
    
    if not is_valid_id(id):
        playsound("Portal2-BuzzerSound.mp3")
        continue
 
    if id not in tapped_ids:
        tapped_ids[id] = 1
    else:
        tapped_ids[id] += 1
    
    if tapped_ids[id] > 2:
        playsound("Portal2-BuzzerSound.mp3")
        print(tapped_ids[id])
    else:
        playsound("Portal2-Beep.mp3")
    
    time.sleep(0.1)
