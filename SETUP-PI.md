# SETUP INSTRUCTIONS

## Below you will find setup instructions for the hardware, many thanks to this post: https://www.submergedcottage.co.uk/blog/network-aquarium-temperature-monitoring-with-raspberry-pi/ as the inspiration for this project.

### Equipment needed:
* 2 pack DS18B20 [temp probes](https://www.amazon.com/gp/product/B094FKQ9BS?psc=1), $8.99 at time of writing
* 1 (or 2) [raspberry pi zero WH](https://www.amazon.com/gp/product/B0CG99MR5W?psc=1), $34.90 at the time of writing
* 1 (or 2) [microSD cards](https://www.amazon.com/SanDisk-Ultra-microSDHC-Memory-Adapter/dp/B08GYBBBBH), $11.86 at time of writing
* 1 (or 2) [Raspberry pi power supply](https://www.amazon.com/Raspberry-Supply-SoulBay-Adapter-Android/dp/B07CVH21NC), $11.39 at time of writing
* (OPTIONAL) [Micro-usb hub (for connecting keyboard and mouse)](https://www.amazon.com/AuviPal-Adapter-Playstation-Classic-Raspberry/dp/B083WML1XB), $7.94 at time of writing
* (OPTIONAL) USB-A keyboard and mouse
* (OPTIONAL) Mini HDMI to HDMI converter or cable to boot the raspberry pi into a GUI

### Steps:
1. Flash a new copy of raspbian to an adequately sized micro SD Card. I chose a 64 GB card just because they were cheap enough. 
    1. First install the Raspberry Pi imager: https://www.raspberrypi.com/software/ 
1. If you are using a raspberry pi zero WH (as above), choose the appropriate OS version. As of this writing it is a port of Debian Bullseye released 2023-12-05 and make sure it is “Legacy 32-bit”. When you open the imager tool, it should be the first option after you choose your raspberry pi. 
1. If you aren’t purchasing the OPTIONAL equipment above, you will want to enable SSH and use the pi “headless”. This just means there is no graphical user interface, everything will be through the command line interface (the terminal). If you aren’t comfortable with the terminal just yet, buy the optional equipment above. 
1. To enable SSH, it is very simple. Once step 1 is complete, safely remove the SD card from your host computer (macOS, Linux, or Windows) that you used to flash the SD card. Then navigate to the boot folder and create a file called “ssh” without a file extension.
    1. Windows: right click in the boot volume’s white space and select New > Text Document. Delete the .txt extension before you hit Enter. If you don’t already see file extensions, click View and enable File name extensions in the menu bar.
    1. Mac/Linux: open the terminal and navigate to the boot directory of your sd card and type:
    * `touch ssh`
    1. Safely remove the sd card from your computer.
    1. Boot up the raspberry pi headless and then SSH into it. [Here is more info if you get hung up.](https://www.raspberrypi.com/documentation/computers/remote-access.html#remote-access)
1. SSH into your raspberry pi, git clone this repo, and add the script to cron per the [README.md](https://github.com/shalloran/aqtempi/blob/main/README.md)
1. Further help:    
    1. [How to setup email alerts in ThingSpeak.](https://blogs.mathworks.com/iot/2020/01/10/send-email-alerts-from-thingspeak/)
    1. [How to automate them every hour.](https://www.mathworks.com/help/thingspeak/timecontrol-app.html)