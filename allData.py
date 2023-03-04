import database
import client
import copyclient
import server
import socket


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
            splitDT[2] = rec_phone_number

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
            phone_numbers = user_collection.find({}, {"phoneNumber": 1}, skip=0)
            for user in phone_numbers:
                if user["phoneNumber"] == fullNumber:
                    print("phoneNumber already exit\n\n\n")
                    return False
            return fullNumber

        else:
            print("not correct")
            return False

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

        db_ph_numbers = user_collection.find_one({"phoneNumber":phoneNumber1})
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
        menu_option = "\n\n           I have this item::\n PRESS 1: soft drink--:# Press 2: Sea Foods--:# Press 3: BBQ--# PRESS 4: " \
                      "Cakes--:# PRESS 5: Foods--:# PRESS 6: show all menu--:"
        return menu_option

    def get_shop_name(self):
        obj2 = database.Mongodatabase()
        collections = obj2.collection
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

    # def get_shop_name(self):
    #     obj2 = database.Mongodatabase()
    #     collections = obj2.collection
    #     # Find all shops that have 'soft drink' menu
    #     shops_with_soft_drinks = collections.find(
    #         {"soft drink": {"$exists": True}})
    #
    #     # Create a dictionary to store shop names with 'soft drink' menu
    #     shop_dict = {}
    #
    #     # Loop through all shops with 'soft drink' menu and add shop names and soft drinks to the dictionary
    #     for shop in shops_with_soft_drinks:
    #         shop_name = shop["Shop Name"]
    #         soft_drinks = {drink["name"]: drink["price"] for drink in shop["soft drink"]}
    #         shop_dict[shop_name] = soft_drinks
    #
    #     # Return the dictionary with shop names and 'soft drink' menu
    #     return shop_dict

    # def get_shop_name(self):
    #     obj2 = database.Mongodatabase()
    #     collections = obj2.collection
    #     # Find all shops that have 'soft drink' menu
    #     shops_with_soft_drinks = collections.find(
    #         {"soft drink": {"$exists": True}})
    #
    #     # Create a dictionary to store shop names with 'soft drink' menu
    #     shop_dict = {}
    #
    #     # Loop through all shops with 'soft drink' menu and add shop names and soft drinks to the dictionary
    #     for shop in shops_with_soft_drinks:
    #         shop_name = shop["Shop Name"]
    #         soft_drinks = []
    #         for drink in shop["soft drink"]:
    #             soft_drink_name = drink["name"]
    #             soft_drink_price = drink["price"]
    #             soft_drinks.append(f"{soft_drink_name} ({soft_drink_price}ks)")
    #         shop_dict[shop_name] = ", ".join(soft_drinks)
    #
    #     # Return the dictionary with shop names and 'soft drink' menu
    #     return shop_dict

    # def get_soft_drinks_menu(self, shop_name):
    #     for data in data1:
    #         if data['Shop Name'] == shop_name:
    #             return data['soft drink']
    #     return None



