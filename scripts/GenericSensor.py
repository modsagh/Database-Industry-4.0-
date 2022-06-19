import socket
import json
import threading
import datetime
import time
from typing_extensions import dataclass_transform

import numpy as np

print_lock = threading.Lock()

class Client():
    def __init__(self, ip, port, connection):
        self.connection = connection
        self.ip = ip
        self.port = port

    def run(self):
        start = time.time()
        while True:
            if start - time.time() > 1/self.fs:
                self.buffer.append(np.random.uniform(self.min_val, self.max_val))


class GenericSensor(threading.Thread):
    def __init__(self, name, serial_number, unit, min_val, max_val, fs, lon, lat, ip_address='localhost') -> None:
        threading.Thread.__init__(self)
        self.name = name
        self.serial_number = serial_number
        self.ip_address = ip_address
        
        self.unit = unit
        self.max_val = max_val
        self.min_val = min_val
        self.fs = fs
        self.lon = lon
        self.lat = lat
        
        self.server = socket.socket()
        self.server.bind((self.ip_address, 0))
        self.port = self.server.getsockname()[1]

        self.clients = []
        self.buffer = []

    def broadcast_val(self):
        while True:
            if len(self.buffer) > 0:
                val = self.buffer.pop(0)
                data = self.measure_to_json(val[0],val[1])
                for client in self.clients:
                    try:
                        client.connection.sendall(str.encode(data))
                    except BrokenPipeError as ex:
                        self.clients.remove(client)

    def measurement_sim(self):
        start = time.time()
        while True:
            if np.abs(start - time.time()) > (1.0/self.fs):
                self.buffer.append((np.random.uniform(self.min_val, self.max_val),time.time()))
                start = time.time()
     
    def run(self):
        thread_measurement_sim = threading.Thread(target = self.measurement_sim)
        thread_measurement_sim.start()

        thread_broadcast_val= threading.Thread(target = self.broadcast_val)
        thread_broadcast_val.start()

        self.server.listen(5)

        while True :
            connection, (ip, port) = self.server.accept()
            client = Client(ip, port, connection)
            self.clients.append(client)    
        self.server.close()

    def measure_to_json(self, val,date):
        dict__ = {'name': self.name,
                'serial_number': self.serial_number, 
                'ip_address': self.ip_address,
                'port': self.port,
                'unit': self.unit,
                'lon':self.lon,
                'lat':self.lat,
                'value': val,
                'date': date
                }
        return json.dumps(dict__)

    def __str__(self) -> str:
        description = 'name: {},\n\tserial_number: {},\n\tip_address: {},\n\tport:{},\n\tunit:{},\n\tlon:{},\n\tlat:{}'.format(
            self.name,
            self.serial_number, 
            self.ip_address,
            self.port,
            self.unit,
            self.lon,
            self.lat,
            )
        return description

if __name__ == "__main__":
    temp_1 = GenericSensor('temperature_1', '2NixMVxg','C', -10, 40, 1000, 19, 22)
    temp_2 = GenericSensor('temperature_2', '2VWFjDQW','C', -10, 40, 10000, 19, 21)

    hum_1 = GenericSensor('humidity_1', '4FZcLPqM','%', 0, 100, 1, 17, 20)
    hum_2 = GenericSensor('humidity_2', '4SLeUtgm','%', 0, 100, 3, 18, 20) 

    lum_1 = GenericSensor('luminosity_1', '55Xxbjbb','lx', 0, 10**5, 100, 17, 20)
    lum_2 = GenericSensor('luminosity_2', '5M5jZxY5','lx', 0, 10**5, 50, 18, 20) 

    temp_1.start()
    temp_2.start()
    
    hum_1.start()
    hum_2.start()
    
    lum_1.start()
    lum_2.start()

    print(temp_1)
    print(temp_2)
    print(hum_1)
    print(hum_2)
    print(lum_1)
    print(lum_2)