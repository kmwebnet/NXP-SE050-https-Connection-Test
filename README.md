# NXP SE050 https-Connection-Test

This communicates NXP SE050 secure chip from ESP32 and connects to test web server.  
it's protected i2c transmission by PlatformSCP03 keys.  

# Requirements

Platformio(PIO Core:4.3.0 PLATFORM: Espressif 32 1.11.1) with VS Code environment.  
install "Espressif 32" platform definition on Platformio  

you need to do provisioning by executing NXP SE050 provisioning-cli prior to use this code.   

# Environment reference
  
  Espressif ESP32-DevkitC  
  this project initialize both of I2C 0,1 port, and the device on I2C port 0 is absent.  
  pin assined as below:  


      I2C 0 SDA GPIO_NUM_18
      I2C 0 SCL GPIO_NUM_19

      I2C 1 SDA GPIO_NUM_21
      I2C 1 SCL GPIO_NUM_22
          
  NXP SE050C1(on I2C port 1)  

  if you use other variants you need to change ENC, MAC, DEK key definition on port/ex_sss_auth.h]  

  Never use this code as production unless you change 3 keys to your own.  

# Usage

"git clone --recursive " on your target directory. and download "Plug & Trust MW Release v02.12.04" from NXP website and put the contents into src as "simw-top" folder. you need to change a serial port number which actually connected to ESP32 in platformio.ini.

replace definitions to your own in main.c

#define EXAMPLE_WIFI_SSID ""
#define EXAMPLE_WIFI_PASS "" 

#define DFL_SERVER_NAME ""
#define DFL_SERVER_PORT ""

# Run this project

just execute "Upload" on Platformio.   

# License

This software is released under the MIT License, see LICENSE.  
