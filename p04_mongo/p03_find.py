from connect_mongo import mydb_pr24

mycol = mydb_pr24["customers"]

print("Find one:")
response = mycol.find_one()
print(response)

print('-' * 80)
print("Find:")
# SELECT * FROM customers;
for response in mycol.find():
    print(response)

print('-' * 80)
print("Find (pouze vybrané atributy)")
for response in mycol.find({}, {"_id": 0, "name": 1, "surname": 1}):
    print(response)

print('-' * 80)
print("Find (zakázané atributy)")
for response in mycol.find({}, {"address": 0, "email": 0, "phone_number": 0}):
    print(response)

"""print('-' * 80)
print("Find (nelze kombinovat výběr a zákaz atributů")
for response in mycol.find({}, {"name": 1, "surname": 1, "address": 0}):
    print(response)"""
# pymongo.errors.OperationFailure: Cannot do exclusion on field address in inclusion projection, full error: {'ok': 0.0, 'errmsg': 'Cannot do exclusion on field address in inclusion projection', 'code': 31254, 'codeName': 'Location31254'}

print("=" * 80)
myquery = {"surname": "Novák"}
print(f"Výsledek dotazu: {myquery}:")
for response in mycol.find(myquery, {"_id": 0, "name": 1, "surname": 1}):
    print(response)

print("-" * 80)
myquery = {"surname": {"$gt": "N"}}
print(f"Výsledek dotazu: {myquery}:")
for response in mycol.find(myquery):
    print(response)

print("-" * 80)
myquery = {"surname": {"$regex": "^N"}}
print(f"Výsledek dotazu: {myquery}:")
for response in mycol.find(myquery):
    print(response)

print("-" * 80)
myquery = {"address": {"$regex": "Ostrava$"}}
print(f"Výsledek dotazu: {myquery}:")
for response in mycol.find(myquery):
    print(response)

print("-" * 80)
myquery = {"surname": "Novák", "address": {"$regex": "Ostrava$"}}
print(f"Výsledek dotazu: {myquery}:")
for response in mycol.find(myquery, {"_id": 0}):
    print(response)
