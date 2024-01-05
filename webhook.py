#!/usr/bin/env python3
# Webhook version

import os
import glob
import datetime
import psutil
import requests

WEB_HOOK_URL = "https://example.webhook.com/YOUR_WEBHOOK_URL_HERE"

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

# sends json payload of date, temp, disk_usage, and memory_usage
data_to_send = {}
data_to_send["date"] = str(datetime.datetime.now())
temp = read_temp()
data_to_send["temp"] = temp
data_to_send["disk_usage"] = psutil.disk_usage("/").percent
data_to_send["memory_usage"] = psutil.virtual_memory().percent

r = requests.post(WEB_HOOK_URL, json = data_to_send)
print(r.text)