#!/usr/bin/env python3
"""Queries Nginx logs for stats"""

from pymongo import MongoClient


def main():
    """Retrieves some nginx stats from db"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    print(f"{nginx.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f"""\tmethod {method}: {nginx.count_documents(
                {"method": method})}"""
              )
    print(f"""{nginx.count_documents({
            "method": "GET", "path": "/status"})} status check"""
          )

    print("IPs:")
    x = 0
    IPs_count = nginx.aggregate([
        {
            '$group': {
                '_id': "$ip",
                'count': {'$sum': 1}
            }
        },
        {
            "$sort": {"count": -1}
        }
    ])

    for i in IPs_count:
        print("\t{}: {}".format(i.get('_id'), i.get('count')))
        x += 1
        if x > 9:
            break


if __name__ == "__main__":
    main()
