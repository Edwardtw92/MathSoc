from typing import Dict
import csv
from playsound import playsound


with open("registered-textbooks.csv", 'r') as csvfile:
    registered = {}
    file = csv.reader(csvfile, delimiter=',')
    for row in file:
        registered[row[0]] = row[1]


def scan():
    while True:
        code = str(input("Scan: ")) 
        if code in registered:
            print('"{0}" Registered\n\n\n\n\n'.format(registered[code]))
            playsound('Portal2-Beep.mp3')
        else:
            print("Not Registered\nPlease register\n\n\n\n\n")
            playsound('Portal2-BuzzerSound.mp3')


scan()
