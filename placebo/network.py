from socket import *
from pickle import loads as pLoads, dumps as pDumps
from json import loads as jLoads, dumps as jDumps

class ServerEvent:
  def __init__(self):
    self.connect = ()
    self.address = ()
    self.data = {}

  def send(self, name, data):
    self.connect.send(pDumps(jDumps({"name": name, "data": data})))

  def set(self, connect, address):
    self.connect = connect
    self.address = address
    self.data = jLoads(pLoads(self.connect.recv(1024)))

class Server:
  def __init__(self, host="127.0.0.1", port=9090):
    self.host = host
    self.port = port

    self.ons = []
    self.event = ServerEvent()
    self.running = True

    self.socket = socket(AF_INET, SOCK_DGRAM)
    self.socket.bind((self.host, self.port))
    self.socket.listen(1000)

  def on(self, name, *methods):
    self.ons.append({
      "name": name,
      "methods": methods
    })

  def run(self):
    connect, address = self.socket.accept()
    while self.running:
      try:
        self.event.set(connect, address)
        for on in self.ons:
          if on["name"] == self.event.data["name"]:
            print(self.event.data)
            on["method"](self.event)
      except Exception as e: pass
    self.socket.close()


class ClientEvent:
  def __init__(self):
    self.socket = socket(AF_INET, SOCK_DGRAM)
    self.data = {}

  def send(self, name, data):
    self.socket.send(pDumps(jDumps({"name": name, "data": data})))

  def set(self, socket):
    self.socket = socket
    self.data = jLoads(pLoads(self.socket.recv(1024)))  

class Client:
  def __init__(self, host="127.0.0.1", port=9090):
    self.host = host
    self.port = port

    self.ons = []
    self.event = ClientEvent()
    self.running = True

    self.socket = socket()
    self.socket.connect((self.host, self.port))

  def on(self, name, *methods):
    self.ons.append({
      "name": name,
      "methods": methods
    })

  def run(self):
    while self.running:
      self.event.set(self.socket)
      for on in self.ons:
        if on["name"] == self.event.data["name"]:
          on["method"](self.event)
    self.socket.close()