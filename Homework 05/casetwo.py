from pymongo import MongoClient

# MongoDB bağlantısı
client = MongoClient('mongodb+srv://<mongodb_connection_string>')

# Veritabanı ve koleksiyon seçimi
db = client.flaskmongodb
collection = db.Users

# Tüm verileri getirme
def get_all_users():
    return list(collection.find())

# İsimde Ahmet olan kullanıcıları getirme
def get_users_by_name(name):
    return list(collection.find({"Name": name}))

# Yaşı 20'den büyük olan kullanıcıları getirme
def get_users_above_age(age):
    return list(collection.find({"Age": {"$gt": age}}))

# Yaşı 25'ten büyük olan ve description'ı 0 olan kullanıcıları getirme
def get_users_above_age_with_description(age, description):
    return list(collection.find({"$and": [{"Age": {"$gt": age}}, {"Description": description}]}))

# Yaşı 45-48 arasında olan kullanıcıları silme
def delete_users_in_age_range(start_age, end_age):
    collection.delete_many({"Age": {"$gte": start_age, "$lte": end_age}})

# Örnek kullanım
print("Tüm kullanıcılar:")
print(get_all_users())

print("\nİsimde Ahmet olan kullanıcılar:")
print(get_users_by_name("Ahmet"))

print("\nYaşı 20'den büyük olan kullanıcılar:")
print(get_users_above_age(20))

print("\nYaşı 25'ten büyük olan ve description'ı 0 olan kullanıcılar:")
print(get_users_above_age_with_description(25, "0"))

delete_users_in_age_range(45, 48)
print("\n45-48 yaş aralığındaki kullanıcılar silindi.")