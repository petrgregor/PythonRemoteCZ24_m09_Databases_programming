import json

from connect_mongo import mydb_pr24

# Use data in medical-data.json to create a new collection: medicaldata
medical_col = mydb_pr24["medicaldata"]

"""
with open('files/medical-data.json') as f:
    data = json.load(f)

    response = medical_col.insert_many(data)

    print(f"To database 'medicaldata' were inserted {len(response.inserted_ids)} documents.")
"""

# Find all rows with procedure_code equal 0F1F4ZC
print("Find all rows with procedure_code equal 0F1F4ZC")
query = {'procedure_code': "0F1F4ZC"}
procedures = medical_col.find(query)
for procedure in procedures:
    print(procedure)

print('-'*80)

# Find patient with patient_id equal 74, print his full name
print("Find patient with patient_id equal 74, print his full name")
query = {'patient_id': 74}
patient = medical_col.find_one(query)
print(f"{patient["first_name"]} {patient["last_name"]}")

print('-'*80)

# Find a procedure performed on 2019-05-24T01:52:37.000Z and
print("Find a procedure performed on 2019-05-24T01:52:37.000Z")
query = {"visit_date.date": "2019-05-24T01:52:37.000Z"}
visits = medical_col.find(query)
for visit in visits:
    print(visit)

# update its procedure code to 0F1F4ZC
print("update its procedure code to 0F1F4ZC")
new_values = {"$set": {"procedure_code": "0F1F4ZC"}}
response = medical_col.update_many(query, new_values)
print(f"Number of updated documents: {response.modified_count}.")
visits = medical_col.find(query)
for visit in visits:
    print(visit)
