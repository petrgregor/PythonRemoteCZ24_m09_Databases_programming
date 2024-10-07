from connect_mongo import mydb_pr24

mycol = mydb_pr24["customers"]

customers = [
    {"name": "Adam", "surname": "Novák", "address": "Hlavní 22, Brno"},
    {"name": "Bedřich", "surname": "Svoboda", "address": "Jarní 1, Praha"},
    {"name": "Ctibor", "surname": "Novotný", "address": "Letní 13, Olomouc"},

    {"_id": 1, "name": "Dan", "surname": "Lejska", "address": "Zimní 25, Ostrava"},
    {"_id": 2, "name": "Evžen", "surname": "Brzobohatý", "address": "Pardubická 125, Ostrava"},
    {"_id": 3, "name": "Filip", "surname": "Novák", "address": "Zelená 12, Ostrava"},
    {"_id": 4, "name": "Gustav", "surname": "Svoboda", "address": "Modrá 1a, Ostrava"},
    {"_id": 5, "name": "Honza", "surname": "Daniel", "address": "Červená 22, Ostrava"},

    {"_id": 6, "name": "Ivana"},
    {"_id": 7, "name": "Jana", "surname": "Bledá", "email": "jana@bleda.cz"},
    {"_id": 8, "name": "Karla", "surname": "Mráčková", "phone_number": "+420777123456"},
]

response = mycol.insert_many(customers)

print(response.inserted_ids)
