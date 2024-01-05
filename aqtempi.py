# 5 JAN 2024 @shalloran GNU GENERAL PUBLIC LICENSE V3
# AqTempPi - A simple Python script to read the temperature from a DS18B20 sensor and send it to ThingSpeak
# See below for crontab example:

# * * * * * /path/to/your/script.py
# * * * * * (sleep 30; /path/to/your/script.py)

import os
import glob
import requests

# GLOBALS
API_KEY = "<INSERT_YOUR_API_KEY_HERE>"

# Initialize the DS18B20 sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    with open(device_file, 'r') as file:
        lines = file.readlines()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

def send_to_thingspeak(temp):
    base_url = 'https://api.thingspeak.com/update'
    payload = {'api_key': API_KEY, 'field1': temp}
    response = requests.get(base_url, params=payload)
    print(response.text)

# Get temperature and send to ThingSpeak
temp = read_temp()
print(f"Temperature: {temp} C")
send_to_thingspeak(temp)