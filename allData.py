import database
# import client
import copyclient
# import server
import socket
import re


class Data:
    def __init__(self):
        pass

    def createAcc(self):
        user = "Enter user_name--:#Enter your phoneNumber--:#Enter your email--:#Enter your password--:#Enter confirm " \
               "password--:"
        return user

    def storeData(self, sData):
        obj2 = database.Mongodatabase()
        id_order = obj2.clients["Delivery"]["User_collection"]
        id_count = id_order.count_documents({}) + 1
        print(id_count)
        splitDT = sData.split("#")
        print(splitDT)
        splitDT.insert(0, id_count)
        print(splitDT)

        if splitDT[5] == splitDT[4]:
            list1 = ["_id", "name", "phoneNumber", "email", "password"]
            splitDT.remove(splitDT[5])

            rec_phone_number = self.checkPhNumber(splitDT[2])
            splitDT[2] = str(rec_phone_number)

            if rec_phone_number != False:
                # splitDT.insert(2, rec_phone_number)
                print(splitDT)
                zipData = zip(list1, splitDT)
                print("your password correct", zipData)
                zp = dict(zipData)
                obj2.collection_1.insert_one(zp)
                print("insert successful")
                return True

            else:
                return False


        else:
            return False

    def checkPhNumber(self, phNumber):
        obj2 = database.Mongodatabase()
        print(type(phNumber))
        intPhNumber = int(phNumber)
        print(type(intPhNumber))
        if len(phNumber) >= 8:
            add_data = "959"
            fullNumber = add_data + phNumber
            print(fullNumber)
            user_collection = obj2.collection_1
            print("hello")
            # phone_numbers = user_collection.find({}, {"phoneNumber": 1}, {"_id": 0})
            phone_numbers = user_collection.find({}, {"_id": 1, "phoneNumber": 1}, skip=0)
            for user in phone_numbers:
                if user["phoneNumber"] == fullNumber:
                    print("phoneNumber already exit\n")
                    print("user ph number", user["phoneNumber"])
                    print(type(user["phoneNumber"]))
                    return False
            return fullNumber

        else:
            print("not correct")
            return False

    def search_ID_with_phNumber(self, phNumber, order_history , amount_history):
        obj2 = database.Mongodatabase()
        add_data = "959"
        fullNumber = add_data + phNumber
        print("fullnumber type", fullNumber)
        cursor = obj2.collection_1.find({})
        for document in cursor:
            ph_no = document.get("phoneNumber")
            print(ph_no)
        ph_number = {"phoneNumber": fullNumber}
        ph_search = obj2.collection_1.find_one(ph_number)
        print("my phone number search by ph_search", ph_search)
        if ph_search is not None:
            id_search = ph_search.get("_id")
            print("my id : search by phone number:", id_search)
            for order in order_history:
                obj2.collection_1.update_one({"_id": id_search}, {"$push": {"history": order}})
                # obj2.collection_1.update_one({"_id": id_search}, {"$pull": {"history": order}})
                # obj2.collection_1.update_one({"_id": id_search}, {"$unset": {"history": 1}})
            obj2.collection_1.update_one({"_id": id_search}, {"$push": {"amount_history": amount_history}})
            # obj2.collection_1.update_one({"_id": id_search}, {"$unset": {"amount_history": 1}})

            print("Orders inserted successfully")

        else:
            print("No document found with the provided phone number in collection")
            ph_search = obj2.collection_2.find_one(ph_number)
            if ph_search is not None:
                id_search = ph_search.get("_id")
                print("my id : search by phone number:", id_search)
                for order in order_history:
                    obj2.collection_2.update_one({"_id": id_search}, {"$push": {"history": order}})

                obj2.collection_2.update_one({"_id": id_search}, {"$push": {"amount_history": amount_history}})
                print("order inserted successfully by no acc user")

            else:
                id_order = obj2.clients["Delivery"]["No_acc_user_collection"]
                id_count = id_order.count_documents({}) + 1
                print("no acc user id count", id_count)
                data = {
                    "_id": id_count,
                    "phoneNumber": fullNumber
                }
                obj2.collection_2.insert_one(data)
                # obj2.collection_2.insert_one({"_id": id_count})
                # obj2.collection_2.update_one({"_id": id_count}, {"$push": {"phoneNumber": fullNumber}})

                # obj2.collection_2.insert_one(0, id_count)
                # obj2.collection_2.insert_one(1, ph_search)
                for order in order_history:
                    obj2.collection_2.update_one({"_id": id_count}, {"$push": {"history": order}})

                obj2.collection_2.update_one({"_id": id_count}, {"$push": {"amount_history": amount_history}})
                print("order insertd successfully in no data history file")





    def login_information(self):
        user = "Enter your phone number--#/Enter your password--:"
        return user

    def login_account(self, rec_InputData):
        obj2 = database.Mongodatabase()
        splitData = rec_InputData.split("#")
        print(splitData)
        user_collection = obj2.collection_1
        print("helloworld")
        phoneNumber = splitData[0]
        password1 = splitData[1]
        add_data = "959"
        fullNumber = add_data + phoneNumber
        phoneNumber1 = fullNumber

        db_ph_numbers = user_collection.find_one({"phoneNumber": phoneNumber1})
        if db_ph_numbers:
            print("\nphone number found")
            stored_password = db_ph_numbers["password"]
            print(stored_password)
            if stored_password == password1:
                print("\n\nright password")
                return True
            else:
                print("\n\nwrong password")
                return False
        else:
            print("\n\nphone number not found")
            return False




    def menuOption(self):
        menu_option = "\n\n           I have this item::\nPRESS 1: soft drink--:#Press 2: Sea Foods--:#Press 3: BBQ--#PRESS 4: Cakes--:#PRESS 5: Foods--:#PRESS 6: show all menu--:"

        return menu_option



    def get_shop_name(self, option):
        obj2 = database.Mongodatabase()
        collections = obj2.collection
        if option == "1":
            # Find all shops that have 'soft drink' menu
            shops_with_soft_drinks = collections.find({"soft drink": {"$exists": True}})

            # Create a dictionary to store shop names with 'soft drink' menu
            shop_dict = {}

            # Loop through all shops with 'soft drink' menu and add shop names and soft drinks to the dictionary
            for shop in shops_with_soft_drinks:
                shop_name = shop["Shop Name"]
                soft_drinks = ", ".join([f"{drink['name']} ({drink['price']}ks)" for drink in shop["soft drink"]])
                shop_dict[shop_name] = soft_drinks

            # Return a formatted string with shop names and 'soft drink' menu
            output_str = ""
            for shop_name, soft_drinks in shop_dict.items():
                output_str += f"\n{shop_name}: {soft_drinks}\n"
            return output_str

        if option == "2":
            shops_with_Sea_Foods = collections.find({"Sea Foods": {"$exists": True}})
            shop_dict = {}
            for shop in shops_with_Sea_Foods:
                shop_name = shop["Shop Name"]
                sea_food = ", ".join([f"{food['name']} ({food['price']}ks)" for food in shop["Sea Foods"]])
                shop_dict[shop_name] = sea_food

            output_str = ""
            for shop_name, sea_food in shop_dict.items():
                output_str += f"\n{shop_name}: {sea_food}\n"
            return output_str


        if option == "3":
            shops_with_BBQ = collections.find({"BBQ": {"$exists": True}})
            shop_dict = {}
            for shop in shops_with_BBQ:
                shop_name = shop["Shop Name"]
                bbq = ", ".join([f"{food['name']} ({food['price']}ks)" for food in shop["BBQ"]])
                shop_dict[shop_name] = bbq

            output_str = ""
            for shop_name, bbq in shop_dict.items():
                output_str += f"\n{shop_name}: {bbq}\n"
            return output_str


        if option == "4":
            shops_with_Cakes = collections.find({"Cakes": {"$exists": True}})
            shop_dict = {}
            for shop in shops_with_Cakes:
                shop_name = shop["Shop Name"]
                cake = ", ".join([f"{food['name']} ({food['price']}ks)" for food in shop["Cakes"]])
                shop_dict[shop_name] = cake

            output_str = ""
            for shop_name, cake in shop_dict.items():
                output_str += f"\n{shop_name}: {cake}\n"
            return output_str


        if option == "5":
            shops_with_foods = collections.find({"foods": {"$exists": True}})
            shop_dict = {}
            for shop in shops_with_foods:
                shop_name = shop["Shop Name"]
                foods = ", ".join([f"{food['name']} ({food['price']}ks)" for food in shop["foods"]])
                shop_dict[shop_name] = foods

            output_str = ""
            for shop_name, foods in shop_dict.items():
                output_str += f"\n{shop_name}: {foods}\n"
            return output_str


    def search_result(self, shops, menu_option1):
        output = ""
        for shop in shops:
            items = shop.split(': ')
            shop_name = items[0]
            item_list = items[1].split(', ')
            i = 1
            for item in item_list:
                name, price = item.split(' (')
                # price = price[:-3]  # to rejuce last three word
                prices = int(re.search(r'\d+', price).group())

                if name == menu_option1:  # check if menu_option1 matches the item name
                    output += f'{shop_name}\n{i}-  {name}: {prices} ks \n'
                    i += 1
        return output

    def search_result1(self, shops):
        for shop in shops:
            items = shop.split(': ')
            shop_name = items[0]
            item_list = items[1].split(', ')
            print('\nShop Name:', shop_name)
            i = 1
            for item in item_list:
                name, price = item.split(' (')
                price = price[:-3]  # to rejuce last three word
                print(f'{i}-  {name}: {price} ks')
                i += 1

    def buy_option(self):
        buyOption = "\nPRESS 1: To cert--:#PRESS 2: To Cancel--:#PRESS 3: To confirm order--:#PRESS 4: To choose more item--:#PRESS 5: To Exit--:"
        return buyOption

    def location(self):
        # address = "\nPRESS 1: If you are from Quater 1 or 2 --:\nPRESS 2: If you are from Quater 3 or 4--:\nPRESS 3: If you are from Quater 5 or 6--:\nPRESS 4:If you are from Quater 7 or 8--:\nPRESS 5: If you are from Quater 9 or 10--:"
        # return address
        print("\nPRESS 1: If you are from Quater 1 or 2 --:")
        print("PRESS 2: If you are from Quater 3 or 4--:")
        print("PRESS 3: If you are from Quater 5 or 6--:")
        print("PRESS 4: If you are from Quater 7 or 8--:")
        print("PRESS 5: If you are from Quater 9 or 10--:")

    def send_to_deli(self, address, data):
        address = int(address)
        obj2 = database.Mongodatabase()
        # Find the document with the _id field equal to address
        document = obj2.collection_3.find_one({"_id": address})
        if document:
            # If the document exists, update its user_order_data array with the new data
            obj2.collection_3.update_one(
                {"_id": address},
                {"$push": {"user_order_data": {"$each": data}}},
                upsert=True
            )
            print("Inserted data into user_order_data array for document with _id =", address)
        else:
            print("No document found with _id =", address)
