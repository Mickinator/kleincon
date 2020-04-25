import RPi.GPIO as GPIO
import time
import mido

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)  # knob 1
GPIO.setup(22, GPIO.IN) # knob 2
GPIO.setup(27, GPIO.IN) # knob 3
GPIO.setup(17, GPIO.IN) # knob 4
GPIO.setup(4, GPIO.IN)  # knob 5
GPIO.setup(12, GPIO.IN) # knob 6
GPIO.setup(25, GPIO.IN) # knob 7
GPIO.setup(24, GPIO.IN) # knob 8
GPIO.setup(23, GPIO.IN) # knob 9
GPIO.setup(18, GPIO.IN) # knob 10
pc = 1
ch = 0
ton = True

# ----------------------------------------- 
def PC():        # Prog Change senden 
    global pc
    global ch
    global ton
    with mido.open_output("USB MIDI Interface MIDI 1") as outport:
        outport.send(mido.Message('control_change',
            channel=ch, control=0, value=0))    #   MSB
        outport.send(mido.Message('control_change',
            channel=ch, control=32, value=0))  #    LSB
        outport.send(mido.Message('program_change',
            channel=ch, program=pc)) #    PC   
        print('CH =', ch,'   ', 'PC = ', pc)
        PerCon()
# -----------------------------------------       
def PerCon():
    global pc
    global ch
    global ton
    while True:  
# Song start         
        if GPIO.input(5) == 0:    
            with mido.open_output("USB MIDI Interface MIDI 1") as outport:
                time.sleep(0.5)
                outport.send(mido.Message('note_on',        
                channel=15, note=27, velocity=65))        
                print('Song Start')
                
# Song Stopp                   
        if GPIO.input(22) == 0:      
            with mido.open_output("USB MIDI Interface MIDI 1") as outport:
                time.sleep(0.5)
                outport.send(mido.Message('note_on',        
                channel=15, note=28, velocity=65))        
                print('Song Stopp')
                
# PC = 1       
        if GPIO.input(27) == 0:
            time.sleep(0.5)
            ch = 0
            pc = 1
            PC()        
# PC = 2       
        if GPIO.input(17) == 0:
            time.sleep(0.5)
            ch = 0
            pc = 2
            PC()        
# PC = 3       
        if GPIO.input(4) == 0:
            time.sleep(0.5)
            ch = 0
            pc = 3
            PC()        
# PC = 4       
        if GPIO.input(12) == 0:
            time.sleep(0.5)
            ch = 0
            pc = 4
            PC()        
# PC = 5       
        if GPIO.input(25) == 0:
            time.sleep(0.5)
            ch = 0
            pc = 5
            PC()        
# PC = 6       
        if GPIO.input(24) == 0:
            time.sleep(0.5)
            ch = 0
            pc = 6
            PC()        
# PC = 7       
        if GPIO.input(23) == 0:
            with mido.open_output("USB MIDI Interface MIDI 1") as outport:
                time.sleep(0.5)
                outport.send(mido.Message('note_on',        
                channel=15, note=9, velocity=65))
                print('All Notes Off')     
# PC = 8       
        if GPIO.input(18) == 0:
            global ton
            time.sleep(0.5) 
            if ton == True:
                with mido.open_output("USB MIDI Interface MIDI 1") as outport:
                    outport.send(mido.Message('control_change',        
                    channel=0, control=64, value=127))   
                print('Damper on')
                ton = not ton
            else:
                with mido.open_output("USB MIDI Interface MIDI 1") as outport:
                    outport.send(mido.Message('control_change',        
                    channel=0, control=64, value=0))   
                print('Damper off')
                ton = not ton  
# ---------------------------------------------------------
PerCon()

