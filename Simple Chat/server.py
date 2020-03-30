from socket import *
try:
    S=socket(AF_INET,SOCK_STREAM)
    S.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    host='127.0.0.1'
    port=7000
    S.bind((host,port))
    S.listen(5)
    C,ad=S.accept()
    print("connection from: ",ad[0])
    while True:
        X=C.recv(2048)
        print("client: ",X.decode('utf-8'))
        C.send(input("server: ").encode('utf-8'))
    S.close()
except error as e:
    print(e)
except KeyboardInterrupt:
    print("chat is terminated !! ")
    

    
