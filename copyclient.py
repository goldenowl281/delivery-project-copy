import socket
import database

class TCPclient:
    def __init__(self):
        self.server_ip = 'localhost'
        self.server_port = 8081

    def main(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.server_ip, self.server_port))
            print("connection success\n")

            while True:
                print("\n\nPRESS 1: TO Create Account")
                print("PRESS 2: TO login Account")
                print("PRESS 3: TO Show Menu")

                option = input("ENTER OPTION_-:")

                if option == "1":
                    client.send(option.encode())
                    rec_from_server = client.recv(4096)
                    print(f'\n[&&]Receive from server :{rec_from_server.decode()}')

                    # get user inputs
                    first_name = input("Enter your First Name: ")
                    phoneNumber = input("Enter your phone number: ")
                    email = input("Enter your Email Address: ")
                    password = input("Enter your Password: ")
                    confirmpassword = input("Enter your confirmPassword: ")


                    # send user inputs to server
                    create_account_data = f"{first_name}#{phoneNumber}#{email}#{password}#{confirmpassword}"
                    client.send(create_account_data.encode())

                elif option == "2":
                    client.send(option.encode())
                    rec_from_server = client.recv(4096)
                    print(f'\n[&&]Receive from server :{rec_from_server.decode()}')

                    # get user inputs
                    phoneNumber = input("Enter your phone number: ")
                    password = input("Enter your Password: ")

                    # send user inputs to server
                    login_account_data = f"{phoneNumber}#{password}"
                    client.send(login_account_data.encode())
                    recData = client.recv(4096)
                    print(recData)

                elif option == "3":
                    client.send(option.encode())

                    # Receive and display menu option from server
                    rec_from_server = client.recv(4096)
                    print(f'\n[&&]Receive from server :{rec_from_server.decode()}\n')
                    rec_from_server = rec_from_server.decode()
                    item = rec_from_server.split("#")
                    # print(item)
                    for menu in item:
                        print(menu)
                    # get user input
                    menu_option = input("Enter your option: ")
                    client.send(menu_option.encode())

                    # Receive and display menu option from server
                    rec_from_server1 = client.recv(4096)
                    print(f'\n[&&]Receive from server :\n{rec_from_server1.decode()}\n')
                    print(type(rec_from_server1))
                    rec_from_server1 = rec_from_server1.decode()
                    print(rec_from_server1)
                    shops = rec_from_server1.split("\n\n")
                    for shop in shops:
                        items = shop.split(': ')
                        shop_name = items[0]
                        item_list = items[1].split(', ')
                        print('\nShop Name:', shop_name)
                        for item in item_list:
                            name, price = item.split(' (')
                            price = price[:-3]
                            print('-', name, ':', price, 'ks')



if __name__ == "__main__":
    tcpClient = TCPclient()
    tcpClient.main()
