#!/usr/bin/env python3
"""Python script that provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection):
    """Provides some stats about Nginx logs stored in MongoDB"""
    
    try:
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

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        client = MongoClient('mongodb://127.0.0.1:27017', serverSelectionTimeoutMS=5000)
        db = client.logs
        nginx_collection = db.nginx

        # Ensure MongoDB connection is working
        client.admin.command('ping')

        log_stats(nginx_collection)

    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
