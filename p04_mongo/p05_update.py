from connect_mongo import mydb_pr24

mycol = mydb_pr24["customers"]

myquery = {"surname": {"$exists": 0}}
print(mycol.find_one(myquery))
new_values = {"$set": {"surname": "Chýlková"}}
mycol.update_one(myquery, new_values)

myquery = {"name": "Ivana"}
print(mycol.find_one(myquery))

print("-" * 80)
print("Změníme příjmení u Jany Bledé:")
myquery = {"name": "Jana", "surname": "Bledá"}
print(mycol.find_one(myquery))
new_values = {"$set": {"surname": "Veselá"}}
mycol.update_one(myquery, new_values)
print(mycol.find_one({"name": "Jana"}))

print("-" * 80)
print("Všem zákazníkům z Ostravy přidáme informaci o kraji.")
myquery = {"address": {"$regex": "Ostrava$"}}
for response in mycol.find(myquery):
    print(response)
new_values = {"$set": {"district": "Moravskoslezský kraj"}}
response = mycol.update_many(myquery, new_values)
print(f"Bylo změněno {response.modified_count} záznamů.")
for response in mycol.find(myquery):
    print(response)
