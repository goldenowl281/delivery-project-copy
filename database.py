import pymongo
from pymongo import MongoClient
import socket


class Mongodatabase:
    try:
        clients = MongoClient('localhost', 27017)
        db = clients['Delivery']

        collection = db['shop-collection']
        collection_1 = db['User_collection']

        print("connection success")
    except Exception as error:
        print(error)

    def __init__(self):
        data = {"_id": 2, "name": "sithu", "phoneNumber": 959970244289, "email": "sithu@gmail.com",
                "password": "sithuaung"}
        # try:
        #     self.collection_1.insert_one(data)
        #     print("insert successful")
        # except Exception as error:
        #     print(error)

        # def option(self):
        #     chooseOption = "PRESS 1: TO Create Account--:#nPRESS 2: TO Sign_in Account--:#PRESS 3: To Show Menu--:"
        #     return chooseOption

        # Press 2: Sea Foods--:# Press 3: BBQ--# PRESS 4: " \
        # "Cakes--:# PRESS 5: Foods--:# PRESS 6: show all menu--:"
        data1 = [
            {
                "_id": 1, "Shop Name": "PanEi",
                "soft drink": [
                    {"name": "coke", "price": 2000},
                    {"name": "sprite", "price": 2000},
                    {"name": "lemonade", "price": 2000},
                    {"name": "Iced Tea", "price": 2000}
                ],
                "foods": [
                    {"name": "shan noodle", "price": 3000},
                    {"name": "coconut chicken noodle", "price": 3000},
                    {"name": "chicken curry", "price": 5000}
                ]
            },
            {
                "_id": 2, "Shop Name": "TeaPro",
                "soft drink": [
                    {"name": "Apple Juice", "price": 3000},
                    {"name": "GrapeFruit Juice", "price": 3000},
                    {"name": "Hot Chocolate", "price": 4000}
                ],
                "foods": [
                    {"name": "NanGyi Toke", "price": 3000},
                    {"name": "Mohinga", "price": 2000},
                    {"name": "chicken liver & Gizzard", "price": 5000}
                ]
            },
            {
                "_id": 3, "Shop Name": "OceanWave",
                "Sea Foods": [
                    {"name": "Fish and Chips", "price": 7000},
                    {"name": "Crab Meat", "price": 10000},
                    {"name": "Salmon", "price": 10000}
                ],
                "BBQ": [
                    {"name": "BBQ special", "price": 20000},
                    {"name": "Spicy Beef Bomb", "price": 20000},
                    {"name": "Chicken Wings", "price": 10000}
                ]
            },
            {
                "_id": 4, "Shop Name": "FudoBakery",
                "Cakes": [
                    {"name": "Butter Cake", "price": 2000},
                    {"name": "Chick-pea Cake", "price": 5000},
                    {"name": "Cheese-Topping Cake", "price": 5000}
                ],
                "soft drink": [
                    {"name": "Strawberry Delight", "price": 3000},
                    {"name": "Ice Thai Tea", "price": 3000},
                    {"name": "Faluda", "price": 4000},
                    {"name": "Burbble Milktea", "price": 3000},
                    {"name": "Blueberry Delight", "price": 3000}
                ]
            }
        ]
        # try:
        #     self.collection.drop()
        #     self.collection.insert_many(data1)
        #     print("insert successful")
        # except Exception as error:
        #     print(error)


if __name__ == "__main__":
    obj = Mongodatabase()
