# a simple server for chat room using socket and threading

import socket
import threading
import logging
import json
import time

class message:
    def __init__(self, message):
        self.message = message
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    def __str__(self):
        return json.dumps(self.__dict__)

class room:
    def __init__(self, name, password=None):
        self.name = name
        self.clients = []
        self.messages = []
        self.pasword = password
    
    def __str__(self):
        return json.dumps(self.__dict__)
    
    

class server:
    def __init__(self, host, port, *args, **kwargs):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.IP = host
        self.PORT = port
        self.clients = []
        self.rooms = {}
        self.sock.bind((self.IP, self.PORT))
        self.sock.listen(5)
        self.acception_thread = threading.Thread(target=self.acception_loop)
        self.acception_thread.start()
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Server started at {}:{}".format(self.IP, self.PORT))
        
    def acception_loop(self):
        while True:
            client, address = self.sock.accept()
            self.clients.append(client)
            
            
s = server("127.0.0.1", 5555)

            
        
        
