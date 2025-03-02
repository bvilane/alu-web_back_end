#!/usr/bin/env python3
"""MongoDB script to analyze Nginx logs and print statistics"""

from pymongo import MongoClient

def log_stats():
    """Displays statistics about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Count total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count logs by method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count status check occurrences
    status_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

    # Get the top 10 most frequent IPs
    print("IPs:")
    top_ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    log_stats()
