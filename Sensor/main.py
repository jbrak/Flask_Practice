import csv
from Temp_function import t
from time import time, sleep


with open('data.csv', mode = 'a') as data:
    data_writer = csv.writer(data, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    
    while True:
        data_writer.writerow([time(),t()])
        data.flush()
        print('bing')
        sleep(300)
        
    