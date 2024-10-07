from connect_mongo import mydb_pr24

mycol = mydb_pr24["customers"]

myquery = {"surname": "Daniel"}
print(f"Výsledek dotazu: {myquery}")
for response in mycol.find(myquery):
    print(response)
mycol.delete_one(myquery)  # smažeme (jeden) záznam
# pro kontrolu vypíšeme znovu
for response in mycol.find(myquery):
    print(response)

print("-" * 80)
print("Smažeme všechny zákazníky z Ostravy:")
myquery = {"address": {"$regex": "Ostrava$"}}
for response in mycol.find(myquery):
    print(response)
response = mycol.delete_many(myquery)
print(f"Bylo smazáno {response.deleted_count} záznamů.")

print("-" * 80)
print("Smažeme všechny záznamy:")
response = mycol.delete_many({})
print(f"Bylo smazáno {response.deleted_count} záznamů.")

print("=" * 80)
print("Databáze je prázdná:")
for response in mycol.find():
    print(response)

print("=" * 80)
print("Smažeme celou kolekci:")
mycol.drop()
