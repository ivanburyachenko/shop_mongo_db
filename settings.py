import pymongo

data = {

    "bot" : {
        "tg_token" : "6232254406:AAGUxtC1rekxDkAZdy3vtv78tHLufIhaTBU",
        "bot_name" : "Scripy Techno Shop",
        "phone_number" : "+380965913761",
        "email" : "scripytechno@gmail.com",
        "address" : "Вулиця Степана Бандери 49A" 
    },

    "db" : {
        "mongo_token" : "mongodb+srv://Logika_ivan_petrov:IbPS6hMS8sZGg50s@logikacluster.bdorooz.mongodb.net/test",
        "mongo_db" : "Scripy_Techno_Shop",
        "mongo_col_users" : "Users",
        "mongo_col_products" : "Products",
    }

}

my_client = pymongo.MongoClient(data["db"]["mongo_token"])
my_db = my_client[data["db"]["mongo_db"]]
my_col_u = my_db[data["db"]["mongo_col_users"]]
my_col_p = my_db[data["db"]["mongo_col_products"]]
