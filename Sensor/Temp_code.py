import os
import glob
import time

os.system('modprobe w1-gpio') # turns on GPIO module
os.system('modprobe w1-therm') # Turns on temperature module

# Finds Device File that holds Temperature Data
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

#Function that reads sensor data
def read_temp_raw():
    f = open(device_file,'r') #Opens the temperature device file
    lines = f.readlines() #Returns text
    f.close()
    return lines

#Convert the value of the sensor into a temerature
def read_temp():
    lines = read_temp_raw() #reading temperature 'device file'
    
    #While the first line does not contain ''YES', wait for
    #0.2s then read the device file again
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    
    #Look for the position of the '=' in the second line of the
    #device file
    equals_pos = lines[1].find('t=')
    
    # If the '=' is foumd, convert the rest of the line after the
    # '=' into degrees celsius then degrees fahrenheit
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string)/ 1000.0
        temp_f = temp_c*9.0/5.0+32.0
        return temp_c, temp_f
    
while True:
    print(read_temp())
    time.sleep(1)