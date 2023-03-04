import socket
import threading
from database import Mongodatabase
import allData

class TCPserver:
    def __init__(self):
        self.server_ip = 'localhost'
        self.server_port = 8081

    def main(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        server.listen(1)
        print(f'\n[#] listening on {self.server_ip}:{self.server_port}')

        while True:
            client, address = server.accept()
            print(f'\n[@] Accepted connection from {address[0]}:{address[1]}')
            client_handler = threading.Thread(target=self.handle_client, args=(client,))
            client_handler.start()

    def handle_client(self, client_socket):
        while True:
            # Receive data from client
            client_data = client_socket.recv(4096).decode()

            if not client_data:
                # No data received, end connection
                break

            # Process client data
            if client_data == "1":
                print("you can create acc now")
                self.sign_up_Acc(client_socket)


            elif client_data == "2":
                # Login account
                print("you can login now")
                self.log_in_Acc(client_socket)

            elif client_data == "3":
                # Show menu
                print("MENU OPTION")
                self.show_menu(client_socket)

            else:
                # Invalid option, send error message to client
                error_message = "Invalid option, please try again"
                client_socket.send(error_message.encode())

        client_socket.close()

    def sign_up_Acc(self, sock):
        obj = allData.Data()
        print("you can create acc now")
        to_create_data = obj.createAcc()
        sock.send(to_create_data.encode())
        while True:
            rec_login_data_from_client = sock.recv(1024).decode("utf-8")
            print("login data type", type(rec_login_data_from_client))
            print(rec_login_data_from_client)

            # splitData = rec_login_data_from_client.split("#")
            # print(splitData)
            returnDt = obj.storeData(rec_login_data_from_client)
            print(returnDt)
            print("return data type sign_in session", type(returnDt))

            if not returnDt:
                sock.send(to_create_data.encode())
            elif returnDt:
                break

    def log_in_Acc(self, sock):
        obj = allData.Data()
        to_login = obj.login_information()
        sock.send(to_login.encode())
        while True:
            login_receive_data = sock.recv(1024).decode("utf-8")
            print("helloworld")
            print("login data type2", type(login_receive_data))
            print(login_receive_data)
            returnData = obj.login_account(login_receive_data)
            print(returnData)
            print("return data type login session-", type(returnData))

            if not returnData:
                sock.send(to_login.encode())
            elif returnData:
                print("\nlogin success success")
                data ="login success "
                sock.send(data.encode())


    def show_menu(self, sock):
        obj = allData.Data()
        menuData = obj.menuOption()
        sock.send(menuData.encode())
        menu_rec_option = sock.recv(1024).decode("utf-8")
        print(menu_rec_option)
        if menu_rec_option == "1":
            obj = allData.Data()
            shop_menu = obj.get_shop_name()
            sock.send(str(shop_menu).encode())
            shop_menu_choice = sock.recv(1024).decode("utf-8")
            # shop_names_str = '\n'.join(shop_names)
            # sock.send(shop_names_str.encode())
            # shop_name = sock.recv(1024).decode("utf-8")
            # print("Received shop name:", shop_name)


            # a = "receive one"
            # sock.send(a.encode())



if __name__ == "__main__":
    tcpServer = TCPserver()
    tcpServer.main()
