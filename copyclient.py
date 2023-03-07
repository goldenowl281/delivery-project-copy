import socket
import database
import allData


class TCPclient:
    def __init__(self):
        self.server_ip = 'localhost'
        self.server_port = 8082

    def main(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.server_ip, self.server_port))
            print("connection success\n")
            flag = True

            while True:
                print("\n\nPRESS 1: TO Create Account")
                print("PRESS 2: TO login Account")
                print("PRESS 3: TO Show Menu")

                option = input("ENTER OPTION_-:")
                obj = allData.Data()
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
                    while flag:
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
                        obj.search_result1(shops)
                        menu_option1 = input("\nI have this item \nSelete what you want to take by name:--:")
                        client.send(menu_option1.encode())
                        found = client.recv(1024).decode("utf-8")

                        if found != "None":
                            print("my order", found)
                            option2_buy = client.recv(1024)
                            option2_buy = option2_buy.decode("utf-8")
                            print("splitlskdk", type(option2_buy))

                            choices = option2_buy.split("#")
                            while True:
                                for menu in choices:
                                    print(menu)
                                option_Buy = input("Enter your option:  ")

                                if option_Buy == "1":
                                    buy_total = input("Choose how many items do you  want--:")
                                    client.send(buy_total.encode())
                                    price = client.recv(4096).decode("utf-8")
                                    print("Your total amount", price)
                                    # for menu in choices:
                                    #     print(menu)
                                    # option_Buy = input("Enter your option:  ")

                                if option_Buy == "5":
                                    client.send(option_Buy.encode())
                                    flag = False

                                if option_Buy == "4":
                                    client.send(option_Buy.encode())
                                    break

                                    flag = False


                        else:
                            print("Item not found.")


if __name__ == "__main__":
    tcpClient = TCPclient()
    tcpClient.main()
