import serial
import requests
import io
import cv2
import requests
import time


port = '/dev/ttyACM0'
brate = 9600
cmd = 'temp'

serial = serial.Serial(port, baudrate = brate, timeout = None)

serial.write(cmd.encode())

def cin_to_server(index,sensor):

    url = (f'http://180.83.19.43:7579/Mobius/HAETAE/raindrop{index}/{sensor}')
    
    headers =	{'Accept':'application/json',
    'X-M2M-RI':'12345',
    'X-M2M-Origin':'SpUuMHvGqsO', # change to your aei
    'Content-Type':'application/vnd.onem2m-res+json; ty=4'
    }

    data =	{
        "m2m:cin": {
            "con": "1"
            }
            }

    r = requests.post(url, headers=headers, json=data)
    
    try:
        r.raise_for_status()
        print(r)
    except Exception as exc:
        print('There was a problem: %s'%(exc))

while True:
    if serial.in_waiting != 0:
        content = serial.readline()
        msg = content.decode()
        
        print(msg)

        if "gas" in msg:
            print("Gas Detected!")
            cin_to_server(1,"gas")
            time.sleep(5)

        elif "water" in msg:
            print("Water Detected")
            cin_to_server(1,"water")   
            time.sleep(5)     
