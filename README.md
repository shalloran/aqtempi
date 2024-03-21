# aqtempi
A raspberry pi zero w based aquatic temperature monitor with publishing to ThingSpeak. Blog post here: https://halloran.blog/aqtempi/

# Purpose

AqTempPi is a simple Python script that reads the temperature from a DS18B20 sensor and sends it to ThingSpeak. It utilizes the 1-Wire interface to communicate with the sensor and the ThingSpeak API to send the temperature data.

## Prerequisites

- Raspberry Pi or similar device with a DS18B20 temperature sensor connected
- Python 3.x installed
- Requests library installed (`pip install requests`)

## Installation

1. Follow instructions [here](https://github.com/shalloran/aqtempi/blob/main/SETUP-PI.md) to setup the raspberry pi and temperature probe.
1. Git clone this repo and you will have the python script on your raspberry pi.
1. You can choose either `aqtempi.py` for ThingSpeak, or `webhook.py` for webhooks. In either case you will have to configure an API key or a webhook URL. Make sure you don't commit those secrets to an online public repo!

## Configuration

Before running the script, make sure to update the `API_KEY` variable in the script with your ThingSpeak API key. You can obtain an API key by signing up for a ThingSpeak account and creating a new channel.

## Usage

The script will read the temperature from the DS18B20 sensor and send it to ThingSpeak. The temperature value will be displayed in the console.

To run the script manually, use the command `python aqtempi.py`.

To schedule the script to run periodically, you can use the crontab. Here's an example of how to do that:

1. First open cronjob file via:

```bash
crontab -e
```

2. Then add these two lines:

```bash
* * * * * /path/to/your/script.py
* * * * * (sleep 30; /path/to/your/script.py)
```

3. Optionally you can add one more line to schedule the raspberry pi to restart weekly on Tuesday at noon: 

```bash
0 12 * * 2 sudo reboot
```
