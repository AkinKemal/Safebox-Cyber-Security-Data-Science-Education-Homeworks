from pymongo import MongoClient
import random

# MongoDB bağlantısı
client = MongoClient('mongodb+srv://<mongodb_connection_string>')

# Veritabanı ve koleksiyon seçimi
db = client.flaskmongodb
collection = db.Users

# 50 adet random veri ekleme
for _ in range(50):
    name = "User" + str(random.randint(1, 100))
    age = random.randint(0, 50)
    job = "Job" + str(random.randint(1, 5))
    description = "1"

    user = {
        "Name": name,
        "Age": age,
        "Job": job,
        "Description": description
    }

    collection.insert_one(user)

print("Veri ekleme tamamlandı.")