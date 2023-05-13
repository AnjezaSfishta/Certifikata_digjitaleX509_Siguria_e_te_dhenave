def sendMessage(message, socket):
   socket.send(message)

def connectToServer(IP, Port):
   try:
       clientSocket = soct.socket()
       clientSocket.connect((IP, Port))

   except ConnectionRefusedError:
       print("Could not connect to the server")
       clientSocket = None
   return clientSocket

message = ""
serverIP = '127.0.0.1'
serverPort = 8000
socket = connectToServer(serverIP, serverPort)
