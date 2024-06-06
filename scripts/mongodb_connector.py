"""

====================================================================
#                                                                  #
#    This script functions as a MongoDB connector It imports       #
#    the processed data set and loads it to MongoDB. Can be        #
#    adapted to other data  sources.                               #
#                                                                  #
#    adapted from: https://www.mongodb.com/docs/drivers/pymongo/   #
#                                                                  #
====================================================================


"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = 'YOUR URL'

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('YOUR API')) # replace YOUR API with your MongoDB API

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Access database
db = client.get_database("BigData")

# Access/create collection
collection = db.get_collection("ObesPovMen")
collection

# Read CSV file using pandas
csv_file = "../datasets/processed/pd_processed_data.csv"
data = pd.read_csv(csv_file)

# Convert DataFrame to dictionary
data_dict = data.to_dict(orient='records')

# Insert data into MongoDB collection
collection.insert_many(data_dict)

# Close connection
client.close()