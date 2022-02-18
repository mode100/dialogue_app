import socket
import requests

PORT = 50000
BUFFER_SIZE = 1024
# get gip
GLOBAL_HOST = socket.gethostbyname(socket.gethostname())
LOCAL_HOST = "127.0.0.1"
print(f"your gip> {GLOBAL_HOST}")

server_socket = None
connection = None

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen(5)
#     while True:
#         (connection, client) = s.accept()
#         try:
#             print('Client connected', client)
#             data = connection.recv(BUFFER_SIZE)
#             print(data.decode())
#             #connection.send(data.upper())
#             connection.send("メッセージを受け取ったよ!".encode())
#         finally:
#             connection.close()

def server_open(host):
    global server_socket
    if server_socket == None:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, PORT))
        server_socket.listen(1)

def server_open_local():
    server_open(LOCAL_HOST)

def server_open_global():
    server_open(GLOBAL_HOST)

def server_close():
    global connection
    global server_socket
    if connection != None:
        server_disconnect()
    if server_socket != None:
        server_socket.close()
        server_socket = None

def server_waiting():
    global connection
    global server_socket
    (connection, _) = server_socket.accept()

def server_send(data):
    global connection
    global server_socket
    if server_socket != None and connection != None:
        connection.send(data.encode())

def server_receive():
    global connection
    global server_socket
    if server_socket != None and connection != None:
        return connection.recv(BUFFER_SIZE).decode()
    return None

def server_disconnect():
    global connection
    global server_socket
    if server_socket != None and connection != None:
        connection.close()
        connection = None

def main():
    print("""<コマンド一覧>
    /ol ... ローカルサーバーを開きます
    /og ... グローバルサーバーを開きます
    /c ... サーバーを閉じます
    /w ... クライアントを待ちます
    /s ... 相手にメッセージを送ります
    /r ... 相手からのメッセージを確認します
    /d ... 通信を切断します
    """)
    while True:
        _command = input("command> ")
        if _command == "/ol":
            server_open_local()
        elif _command == "/og":
            server_open_global()
        elif _command == "/c":
            server_close()
        elif _command == "/w":
            server_waiting()
        elif _command == "/s":
            _send = input("[貴方] ")
            server_send(_send)
        elif _command == "/r":
            _recv = server_receive()
            if _recv != None:
                print("[相手] "+_recv)
            else:
                print("相手からのメッセージはありません")
        elif _command == "/d":
            server_disconnect()
            print("通信を切断しました")

main()
