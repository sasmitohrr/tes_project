import socket     #import module socket
 
#membuat variable baru bernama lis
listenerSocket = socket.socket()
#deklarasi serverIP dan port
alamatserver = "0.0.0.0"
portserver = 2222
 
#bind
listenerSocket.bind((alamatserver,portserver))
#listen
listenerSocket.listen(0)
print ("server ready....")

try :
    while True:
        handlerSocket, addr = listenerSocket.accept()
        #print alamat client yang telah terhubung
        print ("client telah terhubung" + str(addr))
        #membuat looping baru
        while True:
            #membuat variable baru bernama pesan
            pesan = input("masukan pesan anda : ")
            #mengirim pesan kepada client
            handlerSocket.send(pesan.encode())
            #menerima pesan dari client
            pesan = handlerSocket.recv(1024).decode()
            print ("pesan dari client : " + str(pesan))            
            pass
except KeyboardInterrupt:
        pass
