import sys

# Setting path
sys.path.append('../datasets')

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

uri = 'your-connection-string'

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Aceder à DB 
db = client.get_database("BigData")

# Aceder à colecção
collection = db.get_collection("ObesPovMen")

# Read CSV file using pandas
csv_file = "../datasets/processed/dataset_final.csv"
data = pd.read_csv(csv_file)

# Convert DataFrame to dictionary
data_dict = data.to_dict(orient='records')

# Insert data into MongoDB collection
collection.insert_many(data_dict)

# Close connection
client.close()
