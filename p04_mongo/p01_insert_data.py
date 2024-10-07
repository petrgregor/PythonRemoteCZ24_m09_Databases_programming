from connect_mongo import mydb_pr24


mycol = mydb_pr24["test_collection"]

response = mycol.insert_one({"street_name": "Podzimní", "number": 5, "city": "Brno"})

print(response.inserted_id)
