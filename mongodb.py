import pymongo

def add_data_base(name_of_restaran,time,dictionary_of_resturan,address):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[name_of_restaran]
    mycol = mydb[time]
    x = mycol.insert_one({"_id":time,'name_of_resurant':name_of_restaran,'address':address,'information_of_resturan':dictionary_of_resturan})
def get_information_from_data_base(name_of_restaran,time)   
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[name_of_restaran]
    mycol = mydb[time]
    information_of_data_base = mycol.find()
    return information_of_data_base
