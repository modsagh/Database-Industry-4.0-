import socket
import threading            
 
class SensorConnection(threading.Thread):
    def __init__(self, port, ip_address='localhost') -> None:
        threading.Thread.__init__(self)
        self.port = port
        self.ip_address = ip_address
        self.sensor_socket = socket.socket()
        self.buffer = []
    
    def run(self):
        self.sensor_socket.connect((self.ip_address, self.port))
        while True:
            self.buffer.append(self.sensor_socket.recv(1024).decode())

        self.sensor_socket.close()

if __name__ == '__main__':
    temp_1 = SensorConnection(port=55973)
    temp_2 = SensorConnection(port=55974)

    hum_1 = SensorConnection(port=55975)
    hum_2 = SensorConnection(port=55976) 

    lum_1 = SensorConnection(port=55977)
    lum_2 = SensorConnection(port=55978) 

    temp_1.start()
    temp_2.start()
    
    hum_1.start()
    hum_2.start()
    
    lum_1.start()
    lum_2.start()

    while True:
        if len(temp_1.buffer)>0:
            print(temp_1.buffer.pop(0))
        if len(temp_2.buffer)>0:
            print(temp_2.buffer.pop(0))
        if len(hum_1.buffer)>0:
            print(hum_1.buffer.pop(0))
        if len(hum_2.buffer)>0:
            print(hum_2.buffer.pop(0))
        if len(lum_1.buffer)>0:
            print(lum_1.buffer.pop(0))
        if len(lum_2.buffer)>0:
            print(lum_2.buffer.pop(0))