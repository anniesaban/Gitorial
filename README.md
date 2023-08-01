# section1 - Raspberry Pi Pico W 
Raspberry Pi Pico Hi Resolution pin out - https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf

# section2 - Python
## 2.1. create virtual environment:

      ask python to run the venv package ( the first venv ) and create a virtual env named venv  ( the second venv )
      Note: to use a differnet name for yoru virtual environment, replace the 2nd venv with the name you want to use

      python3 -m  venv <venv>

### 2.1.1 activate virtual environemnt:

    The virtual environment activation configures the Python interpreter installed inside the virtual environment as the currently active
    Python that is invoked when you type python in the command line. This activation is temporary, nothing in your system is modified.

    source venv/bin/activate

### 2.1.2. deactivate virtual environment:

    deactivate


## 2.2. Install packagest to help manage the pico board

### 2.2.1. install rshell

      pip install rshell

## 2.3. Install micro python on pico board

     TBD

## 2.4. Run Rshell

     The rshell command will scan the serial connections available in your computer to locate your board.

     After you run rshell, you are left in a new prompt - the rshell prompt.

     rshell prompt look something like:
         Users/anniesaban/Developer/AnnieWorkArea/REPO2/Gitorial>

     When you are in this prompt, you can
          run tasks related to the  microcontroller board,

          to see all rshel type help

          and also start a MicroPython REPL ( "Read-Eval-Print-Loop" ).


## 2.5 Start MicroPython REPL

    repl


## 2.6 On-Board LEDs

    >>> import machine

    led = machine.Pin('WL_GPIO0', machine.Pin.OUT)
    led.value(1)  or led.value(0)
    or
    led.off() or led.on()

## 2.7 configure pin as input and hook a pull up resistor

    >>> import machine
    >>> button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
    >>> button.value()

# 3. Copy code to the board

    $ rshell cp main.py /pyboard
# 4. WiFi setup

## 4.1 Access Point interface - Create an object that represents the access point interface.
    >>> import network
    >>> ap_if = network.WLAN(network.AP_IF)

### 4.1.1 activate / de-activate

    >>> ap_if.active(True)
    >>> ap_if.active(False)

### 4.1.2. query the settings of this interface:

     >>> ap_if.ifconfig()

## 4.2. The Station Interface
     allow you to connect your board to the Wi-Fi network in your home and get access to the Internet through it:

     >>> import network
     >>> sta_if = network.WLAN(network.STA_IF)

### 4.2.1 activate / de-activate

     >>> sta_if.active(True)
     >>> sta_if.active(False)

### 4.2.2. Scan and detect WiFi network

    With the interface activated,
    >>> sta_if.scan()

### 4.2.3. Connect to Wi-Fi router

#### 4.2.3.1. using SSID and password.  DO NOT SAVE  YOUR UID/PSWD TO YOUR GIT !!!!

        You can then ensure that the connection was made with isconnected():

        >>> sta_if.connect('your SSID', 'your Wi-Fi password')
        >>> sta_if.isconnected()

#### 4.2.3.2. Using Config file - Recommended ( KEEP YOUR Config file local, DO NOT SAVE IT TO GIT!!! )

        Create a new file called config.py with the following contents:
        WIFI_SSID = 'your SSID'
        WIFI_PASSWORD = 'your Wi-Fi password'

        when you need to connect to your Wi-Fi network,  do it without having to write your password:

        - upload config file to your controller board. Using rshell:
            (venv) $ rshell cp config.py /pyboard

        - when you need to connect to your Wi-Fi network:
            >>> import config
            >>> import network
            >>> sta_if = network.WLAN(network.STA_IF)
            >>> sta_if.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
            >>> sta_if.isconnected()


Grinberg, Miguel. MicroPython for the Raspberry Pi Pico W: A gentle introduction to programming digital circuits with Python (p. 60). Miguel Grinberg. Kindle Edition.
### 4.2.4. get the parameters of the connection:

       >>> sta_if.ifconfig()

