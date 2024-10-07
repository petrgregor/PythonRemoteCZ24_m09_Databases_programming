import pymongo

# vytvoření klienta
#mongo_client = pymongo.MongoClient("127.0.0.1", 27017)
mongo_client = pymongo.MongoClient("mongodb://127.0.0.1:27017")


# vytvoření databáze
mydb_test24 = mongo_client.test_db24
mydb_pr24 = mongo_client["PythonRemoteCZ24"]


if __name__ == '__main__':
    print(f"mongo_client: {mongo_client}")
    print(f"mydb_test24: {mydb_test24}")
    print(f"mydb_pr24: {mydb_pr24}")

    databases = mongo_client.list_database_names()
    print(f"databases: {databases}")

    # vytvoření kolekce
    customers_collection = mydb_pr24["customers"]
    