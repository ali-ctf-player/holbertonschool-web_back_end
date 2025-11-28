#!/usr/bin/env python3
"""It is doc string"""
from pymongo import MongoClient

def log_stats():
    """It is doc string"""

    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collections = db.nginx

    total_logs = collections.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET","POST","PUT","PATCH","DELETE"]

    for method in methods:
        number_of_methods = collections.count_documents({"method":method})
        print(f"    method {method}: {number_of_methods}")
    
    check_status = collections.count_documents({"method":"GET","path":"/status"})
    print(f"{check_status} status check")

if __name__ == "__main__":
    log_stats()
