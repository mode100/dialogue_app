import socket
import os
import json

HOST = "127.0.0.1"
PORT = 50000
BUFFER_SIZE = 1024

client_socket = None

folder = os.path.split(__file__)[0] + "/"
filename = "setting.json"

if os.path.isfile(folder+filename):
    with open(folder+filename) as f:
        jsn = json.load(f)
    try:
        HOST = jsn["ip"]
        PORT = jsn["port"]
    except:
        pass
        
print(f"host> {HOST}\nport> {PORT}")

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # s.connect((HOST, PORT))
    
    # data = input('Please input > ')
    # s.send(data.encode())
    # print("通信相手からのメッセージ: "+s.recv(BUFFER_SIZE).decode())

    # while True:
    #     pass

def client_connect(host, port):
    global client_socket
    if client_socket == None:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))

def client_send(data):
    global client_socket
    if client_socket != None:
        client_socket.send(data.encode())

def client_disconnect():
    global client_socket
    if client_socket != None:
        client_socket.close()
        client_socket = None

def client_receive():
    global client_socket
    if client_socket != None:
        return client_socket.recv(BUFFER_SIZE).decode()
    return None

def main():
    print("""<コマンド一覧>
    /c ... 設定されたホストに接続します
    /s ... 相手にメッセージを送ります
    /r ... 相手からのメッセージを確認します
    /d ... 通信を切断します
    """)
    while True:
        _command = input("command> ")
        if _command == "/c":
            try:
                client_connect()
            except:
                print("接続に失敗しました")

        elif _command == "/s":
            _send = input("[貴方] ")
            client_send(_send)
        elif _command == "/r":
            _recv = client_receive()
            if _recv != None:
                print("[相手] "+_recv)
            else:
                print("相手からのメッセージはありません")
        elif _command == "/d":
            client_disconnect()
            print("通信を切断しました")

main()
