import socket
import threading
import database
# from database import Mongodatabase
import allData
import re


list_cert = []
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
        obj2 = database.Mongodatabase()
        obj = allData.Data()
        menuData = obj.menuOption()
        sock.send(menuData.encode())
        menu_rec_option = sock.recv(1024).decode("utf-8")
        print(menu_rec_option)
        if menu_rec_option in ["1", "2", "3", "4", "5"]:
            obj = allData.Data()
            shop_menu = obj.get_shop_name(menu_rec_option)
            print(shop_menu)
            print(type(shop_menu))
            sock.send(str(shop_menu).encode())
            shop_menu_choice = sock.recv(1024).decode("utf-8")

            print(shop_menu_choice)
            shop_menu = shop_menu.split("\n\n")
            found = obj.search_result(shop_menu, shop_menu_choice)
            print(found)
            print(type(found))

            if found:
                sock.send(found.encode())  # Send back the response as a string
                hello_receive = sock.recv(1024).decode("utf-8")
                if hello_receive == '1':
                    buy_options = obj.buy_option()
                    sock.send(buy_options.encode())
                    receive_from_client = sock.recv(1024).decode("utf-8")

                    print("hello", receive_from_client)
                    # try:
                    #     if receive_from_client.strip() == "":
                    #         error_message = "Invalid input, please enter a number"
                    #         sock.send(error_message.encode())
                    #     else:
                    #         receive_from_client = int(receive_from_client)
                    # except ValueError:
                    #     error_message = "Invalid input. Please enter a valid integer."
                    #     sock.send(error_message.encode())
                    #     return self.show_menu(sock)
                    # print("shop name ", shop_names)
                    parts = found.split(": ")
                    shop_name, item_name = parts[0].split(" ", 1)  # split at the first whitespace, limit the split to 2 parts
                    item_price = parts[1].split()[0]  # split at whitespace, get the first element
                    pattern = re.compile(r'[A-Za-z]+\b')
                    shop_name = pattern.findall(shop_name)
                    print("shop type data", type(shop_name))
                    shop_names = str(shop_name[0])  # take the first (and only) element of the shop_name list
                    print("after change shop type data", type(shop_names))

                    print("shop_name:", shop_names)
                    print("item_name:", item_name)
                    print("price:", item_price)
                    # price = found.split(": ")
                    # shop_name = price[0].split('\n')[1]
                    # item_info = price[1].split(", ")
                    # item_name = item_info[0].split(": ")[1]
                    # item_price = item_info[2].split(":")[1].strip()

                    item_price = int(item_price)  # to change string into int
                    print(item_price)
                    print(type(item_price))
                    print(type(receive_from_client))
                    receive_from_client = int(receive_from_client)
                    return_price = item_price * receive_from_client
                    print("total fees", return_price)
                    sock.send(str(return_price).encode())
                    in_user_cert = {f"Shop Name: {shop_names}, item name: {item_name}, item_price: {item_price}ks, item_total: {receive_from_client}, total amount: {str(return_price)}ks"}
                    in_user_certs = str(in_user_cert.pop())
                    list_cert.append(in_user_certs)
                    print("in my cert", list_cert)
                    print("my_cert data type", type(in_user_certs))

                    receive_from_client2 = sock.recv(1024).decode("utf-8")

                    if receive_from_client2 == "5":
                        self.show_menu(sock)

                    elif receive_from_client2 == "4":
                        self.show_menu(sock)


                    elif receive_from_client2 == "3":
                        print("receive from three")
                        list_certs = '\n'.join(str(c) for c in list_cert).encode('utf-8')  # convert each item to string before joining

                        sock.send(list_certs)
                        # print("----------333333", list_certs)
                        rec_address = sock.recv(1024).decode("utf-8")
                        # if rec_address == "1":
                        #     obj2.collection_3.
                        obj.send_to_deli(rec_address, list_cert)

                        rec_total_amount = sock.recv(1024).decode("utf-8")
                        print('total amount', rec_total_amount)
                        print("send successfully")
                        while True:
                            rec_ph_number_from_client = sock.recv(1024).decode("utf-8")
                            print(type(rec_ph_number_from_client), rec_ph_number_from_client)
                            # rec_ph_number_from_client = int(rec_ph_number_from_client)
                            if len(rec_ph_number_from_client) >= 8:
                                phone_no_check = obj.checkPhNumber(rec_ph_number_from_client)

                                if phone_no_check == False:
                                    obj.search_ID_with_phNumber(rec_ph_number_from_client, list_cert, rec_total_amount)
                                    break

                                else:
                                    obj.search_ID_with_phNumber(rec_ph_number_from_client, list_cert, rec_total_amount)
                                    break

                            else:
                                print("please enter phone number correctly :lenghts must be at least 8")
                                numberPhone = False
                                sock.send(bytes(str(numberPhone), 'utf-8'))




            else:
                sock.send("None".encode())  # If item not found, send "None" as a string

        elif menu_rec_option in ["4", "5"]:
            self.show_menu(sock)

        else:
            sock.send("Invalid input. Please enter a valid option.".encode())
            return self.show_menu(sock)




















if __name__ == "__main__":
    tcpServer = TCPserver()
    tcpServer.main()
