from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri="mongodb+srv://ArmaanJoshi:armaan1234@cluster0.xmkxiwh.mongodb.net/?appName=Cluster0"
client=MongoClient(uri)

df=pd.read_csv("D:\\CODING\\Python\\SENSORPROJECT\\notebooks\\wafer_23012020_041211.csv")
# print(df.head())
df=df.drop("Unnamed: 0",axis=1)
json_record=list(json.loads(df.T.to_json()).values())
client["SensorFault"]["waferfault"].insert_many(json_record)