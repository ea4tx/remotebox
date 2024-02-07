Remote Control 
==============

With the ARS-USB, you will also be able to control the antenna motor remotely.

While there are several options such as leaving the remote computer turned on and using AnyDesk or Teamviewer to connect to the remote computer, perhaps the most effective and interesting option is to use a **Raspberry Pi** (RPi), **Rock 3**, or similar mini-computer.

.. Note:: 
    Since 2020, due to component issues, obtaining Raspberry Pi 3 or 4 became quite complicated, and prices soared.
    In 2023, I found an alternative to the Raspberry Pi and started supplying Rock3 devices, which offer much more interesting prices and features than the Raspberry Pi.
    However, both the Rock3 and the Raspberry Pi use the same operating system, so all the software that runs on a Rock3 also works on the Raspberry Pi or other alternatives like Orange Pi, etc.

----------

These mini-computers run a reduced version of Linux, and the ARS-USB (or other EA4TX equipment like the RemoteBox) can be connected to any of the 4 USB ports they include. The Linux OS detects the ARS-USB and creates a serial port, which in this case is called: /dev/ttyACM0.
Using software called **ser2net**, we can route that serial port to the TCP/IP world, allowing the ARS-USB to be accessible via TCP/IP.

Additionally, using a mini-computer results in minimal power consumption.

There are likely more options for remote control of the motor with the ARS-USB, but here we will describe 3 options that I consider interesting:
    
    - ✅ Ser2net: This is the simplest option. It allows a program to connect via TCP/IP and access the ARS-USB. For example, if we want to use **ARSVCOM**
    - ✅ remoteRotator: In addition to using ser2net as in the previous case, remoteRotator provides a web interface, accessible from mobile devices, tablets, etc.
    - ✅ Node-RED: Node-RED is an IoT platform that has become very popular and provides a graphical interface in addition to being widely used in the amateur radio world.

.. toctree::
   :maxdepth: 2
   
   rspi/ser2net
   rspi/remoterotator
   rspi/nodered
   