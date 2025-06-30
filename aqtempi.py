# 5 JAN 2024 @shalloran GNU GENERAL PUBLIC LICENSE V3
# AqTempPi - A simple Python script to read the temperature from a DS18B20 sensor and send it to ThingSpeak
# See below for crontab example:

# * * * * * /path/to/your/script.py
# * * * * * (sleep 30; /path/to/your/script.py)

import os
import glob
import time
import requests
import sys

# GLOBALS
API_KEY = "<INSERT_YOUR_API_KEY_HERE>"

# Initialize the DS18B20 sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'

# FIX BUG 2: Add error handling for sensor detection
try:
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
except IndexError:
    print("Error: No DS18B20 temperature sensor found. Please check your wiring and sensor connection.")
    sys.exit(1)

def read_temp_raw():
    try:
        with open(device_file, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: Unable to read sensor data from {device_file}")
        return None
    except IOError as e:
        print(f"Error reading sensor: {e}")
        return None

def read_temp():
    max_retries = 5
    retry_count = 0
    
    while retry_count < max_retries:
        lines = read_temp_raw()
        if lines is None:
            return None
            
        # Check if sensor reading is valid
        if len(lines) >= 2 and lines[0].strip()[-3:] == 'YES':
            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                try:
                    temp_string = lines[1][equals_pos+2:]
                    temp_c = float(temp_string) / 1000.0
                    return temp_c
                except ValueError:
                    print("Error: Invalid temperature data format")
                    return None
        
        retry_count += 1
        time.sleep(0.2)
    
    print("Error: Failed to get valid temperature reading after maximum retries")
    return None

def send_to_thingspeak(temp):
    # FIX BUG 3: Add proper error handling and timeout for network requests
    base_url = 'https://api.thingspeak.com/update'
    payload = {'api_key': API_KEY, 'field1': temp}
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(base_url, params=payload, timeout=10)
            response.raise_for_status()  # Raise an exception for bad status codes
            print(f"Successfully sent temperature to ThingSpeak: {response.text}")
            return True
        except requests.exceptions.Timeout:
            print(f"Timeout error on attempt {attempt + 1}/{max_retries}")
        except requests.exceptions.ConnectionError:
            print(f"Connection error on attempt {attempt + 1}/{max_retries}")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error on attempt {attempt + 1}/{max_retries}: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Request error on attempt {attempt + 1}/{max_retries}: {e}")
        
        if attempt < max_retries - 1:
            time.sleep(2)  # Wait before retrying
    
    print("Error: Failed to send data to ThingSpeak after all retry attempts")
    return False

# Main execution with error handling
if __name__ == "__main__":
    temp = read_temp()
    if temp is not None:
        print(f"Temperature: {temp} C")
        send_to_thingspeak(temp)
    else:
        print("Failed to read temperature from sensor")
        sys.exit(1)