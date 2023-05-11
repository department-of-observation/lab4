import time
from time import sleep

from hal import hal_led as led
from hal import hal_input_switch as switch
def blink_led(delay,status):
    # Led Blink

    if(status=='left'):
      led.set_output(0, 1)
      time.sleep(delay)

      led.set_output(0, 0)
      time.sleep(delay)


    if(status=='right'):
      for marker in range(0, 25, 1):
         led.set_output(0, 1)
         time.sleep(delay)


         led.set_output(0, 0)
         time.sleep(delay)


def main():
    switch.init()
    led.init()
    for i in range(0, 6666, 1):
       if(switch.read_slide_switch()==1):

         blink_led(0.2,'left')
       if(switch.read_slide_switch()==0):

         blink_led(0.1,'right')
         break





if __name__ == "__main__":
    main()