#!/usr/bin/python3
import requests
import csv
"""restfulAPI week ft.requests & csv"""


url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Target Func 1"""
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts_data = response.json()
        for post in posts_data:
            print(post["title"])
    else:
        print("Failed to fetch data.")


def fetch_and_save_posts():
    """Target Func 2"""
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

    posts_data = [{
        "id": post["id"],
        "title": post["title"],
        "body": post["body"]
    } for post in posts]

    with open("posts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(posts_data)
