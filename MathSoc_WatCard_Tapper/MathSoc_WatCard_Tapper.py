from typing import Dict
import time
from playsound import playsound


tapped_ids = {}

while True:
  id = str(input('Tap WatCard: '))
  current_time = time.localtime()
  # check if time is 0:00
  if current_time.tm_hour == 0 and current_time.tm_min == 0:
        # Reset the list of tapped IDs
        tapped_ids = {}

  if id in tapped_ids:
    if tapped_ids[id] >= 2:
        playsound('Portal2-BuzzerSound.mp3')
        print(tapped_ids[id])
    tapped_ids[id] += 1
  else:
    playsound('Portal2-Beep.mp3')
    tapped_ids[id] = 1
  
  print(tapped_ids)
  time.sleep(1)
