#!/usr/bin/env python3
"""Python script that provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection):
    """Provides some stats about Nginx logs stored in MongoDB"""
    
    # Count total logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Count logs by method
    print("Methods:")
    for method in METHODS:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # Count status check occurrences
    status_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    log_stats(nginx_collection)
