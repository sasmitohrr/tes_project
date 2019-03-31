import socket   #memanggil module socket
 
#deklarasi socket
handlerSocket = socket.socket()
#deklarasi serverIp dan serverport
serverIP = "127.0.0.1"
serverPort = 2222
#menghubungkan
handlerSocket.connect((serverIP,serverPort))
print ("conected to server ........")
try :
    while True:
        #meneriama pesan dari server
        pesan = handlerSocket.recv(1024).decode()
        print ("pesan dari server : " + str(pesan))
        #mengirim pesan kepda server
        pesan = input("masukan pesan anda : ")
        handlerSocket.send(pesan.encode())
except KeyboardInterrupt:
    pass
