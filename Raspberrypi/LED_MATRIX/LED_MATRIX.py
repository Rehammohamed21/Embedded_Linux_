import RPi.GPIO as GPIO  #calling for header file which helps in using GPIO’s of PI

import time            #calling for time to provide delays in program

GPIO.setwarnings(False)  #do not show any warnings

x=1

y=1

GPIO.setmode (GPIO.BCM)  #programming the GPGPIO by BCM pin numbers. (like PIN29 as'GPIO5')

GPIO.setup(12,GPIO.OUT)  #initialize GPIO12 as an output.

GPIO.setup(22,GPIO.OUT)  #initialize GPIO22 as an output.

GPIO.setup(27,GPIO.OUT)

GPIO.setup(25,GPIO.OUT)

GPIO.setup(17,GPIO.OUT)

GPIO.setup(24,GPIO.OUT)

GPIO.setup(23,GPIO.OUT)

GPIO.setup(18,GPIO.OUT)

GPIO.setup(21,GPIO.OUT)

GPIO.setup(20,GPIO.OUT)

GPIO.setup(26,GPIO.OUT)

GPIO.setup(16,GPIO.OUT)

GPIO.setup(19,GPIO.OUT)

GPIO.setup(13,GPIO.OUT)

GPIO.setup(6,GPIO.OUT)

GPIO.setup(5,GPIO.OUT)


PORTVALUE = [128,64,32,16,8,4,2,1]

#value of pin in each port 

A=[0,0b01111111,0b11111111,0b11001100,0b11001100,0b11001100,0b11111111,0b01111111]

#B =[0,0b00111100,0b01111110,0b11011011,0b11011011,0b11011011,0b11111111,0b11111111]

#C= [0,0b11000011,0b11000011,0b11000011,0b11000011,0b11100111,0b01111110,0b00111100]

D=[0,0b01111110,0b01111110,0b11000011,0b11000011,0b11000011,0b11111111,0b11111111]

E=[0,0b11011011,0b11011011,0b11011011,0b11011011,0b11011011,0b11111111,0b11111111]

#F=[0,0b11011000,0b11011000,0b11011000,0b11011000,0b11011000,0b11111111,0b11111111]

#G=[0b00011111,0b11011111,0b11011000,0b11011011,0b11011011,0b11011011,0b11111111,0b11111111]

H=[0,0b11111111,0b11111111,0b00011000,0b00011000,0b00011000,0b11111111,0b11111111]

#I=[0b11000011,0b11000011,0b11000011,0b11111111,0b11111111,0b11000011,0b11000011,0b11000011]

#J=[0b11000000,0b11000000,0b11000000,0b11111111,0b11111111,0b11000011,0b11001111,0b11001111]

#K=[0,0b11000011,0b11100111,0b01111110,0b00111100,0b00011000,0b11111111,0b11111111]

#L=[0b00000011,0b00000011,0b00000011,0b00000011,0b00000011,0b00000011,0b11111111,0b11111111]

M=[0b11111111,0b11111111,0b01100000,0b01110000,0b01110000,0b01100000,0b11111111,0b11111111]

#N=[0b11111111,0b11111111,0b00011100,0b00111000,0b01110000,0b11100000,0b11111111,0b11111111]

O=[0,0b01111110,0b11111111,0b11000011,0b11000011,0b11000011,0b11111111,0b01111110]

#P=[0,0b01110000,0b11111000,0b11001100,0b11001100,0b11001100,0b11111111,0b11111111]

#Q=[0b01111110,0b11111111,0b11001111,0b11011111,0b11011011,0b11000011,0b11111111,0b01111110]

R=[0b01111001,0b11111011,0b11011111,0b11011110,0b11011100,0b11011000,0b11111111,0b11111111]

#S=[0b11001110,0b11011111,0b11011011,0b11011011,0b11011011,0b11011011,0b11111011,0b01110011]

#T=[0b11000000,0b11000000,0b11000000,0b11111111,0b11111111,0b11000000,0b11000000,0b11000000]

#U=[0b11111110,0b11111111,0b00000011,0b00000011,0b00000011,0b00000011,0b11111111,0b11111110]

#V=[0b11100000,0b11111100,0b00011110,0b00000011,0b00000011,0b00011110,0b11111100,0b11100000]

#W=[0b11111110,0b11111111,0b00000011,0b11111111,0b11111111,0b00000011,0b11111111,0b11111110]

#X=[0b01000010,0b11100111,0b01111110,0b00111100,0b00111100,0b01111110,0b11100111,0b01000010]

#Y=[0b01000000,0b11100000,0b01110000,0b00111111,0b00111111,0b01110000,0b11100000,0b01000000]

#Z=[0b11000011,0b11100011,0b11110011,0b11111011,0b11011111,0b11001111,0b11000111,0b11000011]


def PORT(pin):  #assigning GPIO state by taking 'pin' value

    if(pin&0x01 == 0x01):

        GPIO.output(21,0)   #if bit0 of 8bit 'pin' is true pull PIN21 low

    else:

        GPIO.output(21,1)   #if bit0 of 8bit 'pin' is false pull PIN21 high

    if(pin&0x02 == 0x02):

        GPIO.output(20,0)   #if bit1 of 8bit 'pin' is true pull PIN20 low

    else:

        GPIO.output(20,1)   #if bit1 of 8bit 'pin' is false pull PIN20 high

    if(pin&0x04 == 0x04):

        GPIO.output(26,0)   #if bit2 of 8bit 'pin' is true pull PIN26 low

    else:

        GPIO.output(26,1)   #if bit2 of 8bit 'pin' is false pull PIN26 high

    if(pin&0x08 == 0x08):

        GPIO.output(16,0)

    else:

        GPIO.output(16,1)

    

    if(pin&0x10 == 0x10):

        GPIO.output(19,0)

    else:

        GPIO.output(19,1)

    if(pin&0x20 == 0x20):

        GPIO.output(13,0)

    else:

        GPIO.output(13,1)

    if(pin&0x40 == 0x40):

        GPIO.output(6,0)

    else:

        GPIO.output(6,1)

    if(pin&0x80 == 0x80):

        GPIO.output(5,0)

    else:

        GPIO.output(5,1)


def PORTP(pinp):    #assigning GPIO logic for positive terminals by taking 'pinp' value

    if(pinp&0x01 == 0x01): 

        GPIO.output(12,1)     #if bit0 of 8bit 'pinp' is true pull PIN12 high

    else:

        GPIO.output(12,0)     #if bit0 of 8bit 'pinp' is false pull PIN12 low

    if(pinp&0x02 == 0x02):

        GPIO.output(22,1)     #if bit1 of 8bit 'pinp' is true pull PIN22 high

    else:

        GPIO.output(22,0)     #if bit1 of 8bit 'pinp' is false pull PIN22 low

    if(pinp&0x04 == 0x04):

        GPIO.output(27,1)     #if bit2 of 8bit 'pinp' is true pull PIN27 high

    else:

        GPIO.output(27,0)     #if bit2 of 8bit 'pinp' is false pull PIN27 low

    if(pinp&0x08 == 0x08):

        GPIO.output(25,1)

    else:

        GPIO.output(25,0)

    if(pinp&0x10 == 0x10):

        GPIO.output(17,1)

    else:

        GPIO.output(17,0)

    if(pinp&0x20 == 0x20):

        GPIO.output(24,1)

    else:

        GPIO.output(24,0)

    if(pinp&0x40 == 0x40):

        GPIO.output(23,1)

    else:

        GPIO.output(23,0)

    if(pinp&0x80 == 0x80):

        GPIO.output(18,1) #if bit7 of 8bit 'pinp' is true pull PIN18 high

    else:

        GPIO.output(18,0) #if bit7 of 8bit 'pinp' is false pull PIN18 low


while 1:
	
	#writing "REHAM MOHAMED"
    for y in range (100):   #execute loop 100 times

        for x in range (8): #execute the loop 8 times incrementing x value from zero to seven

            pin  = PORTVALUE[x]  #assigning value to 'pin' for each digit

            PORT(pin);  #mapping appropriate GPIO 

            pinp= R[x]  #assigning character 'R' value to 'pinp' 

            PORTP(pinp); #turning the GPIO to show character 'R'

            time.sleep(0.0005) #wait for 0.5msec


    for y in range (100):

        for x in range (8):

            pin  = PORTVALUE[x]

            PORT(pin);

            pinp= E[x]

            PORTP(pinp);

            time.sleep(0.0005)

    

    for y in range (100):

        for x in range (8):

            pin  = PORTVALUE[x]

            PORT(pin);

            pinp= H[x]

            PORTP(pinp);

            time.sleep(0.0005)


    for y in range (100):

        for x in range (8):

            pin  = PORTVALUE[x]

            PORT(pin);

            pinp= A[x]

            PORTP(pinp);

            time.sleep(0.0005)


    for y in range (100):

        for x in range (8):

            pin  = PORTVALUE[x]

            PORT(pin);

            pinp= M[x]

            PORTP(pinp);

            time.sleep(0.0005)

    pinp= 0

    PORTP(pinp);

    time.sleep(0.5)  
            

    for y in range (100):

        for x in range (8):

            pin  = PORTVALUE[x]

            PORT(pin);

            pinp= M[x]

            PORTP(pinp);

            time.sleep(0.0005)


    for y in range (100):

        for x in range (8):

            pin  = PORTVALUE[x]

            PORT(pin);

            pinp= O[x]

            PORTP(pinp);

            time.sleep(0.0005)


    for y in range (100):

        for x in range (8):

            pin  = PORTVALUE[x]

            PORT(pin);

            pinp= H[x]

            PORTP(pinp);

            time.sleep(0.0005)

            

    for y in range (100):

        for x in range (8):

            pin  = PORTVALUE[x]

            PORT(pin);

            pinp= A[x]

            PORTP(pinp);

            time.sleep(0.0005)


    for y in range (100):

        for x in range (8):

            pin  = PORTVALUE[x]

            PORT(pin);

            pinp= M[x]

            PORTP(pinp);

            time.sleep(0.0005)

            

    for y in range (100):

        for x in range (8):

            pin  = PORTVALUE[x]

            PORT(pin);

            pinp= E[x]

            PORTP(pinp);

            time.sleep(0.0005)

            

    for y in range (100):

        for x in range (8):

            pin  = PORTVALUE[x]

            PORT(pin);

            pinp= D[x]

            PORTP(pinp);

            time.sleep(0.0005)



    pinp= 0

    PORTP(pinp);

    time.sleep(1)     