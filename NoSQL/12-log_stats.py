#!/usr/bin/env python3
"""
Python script that provides stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']
    
    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # Status check count
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

except Exception as e:
    print("0 logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f"\tmethod {method}: 0")
    print("0 status check")
