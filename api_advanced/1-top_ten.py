#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Prints the first 10 hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_dev)"}
    params = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    try:
        posts = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return
    for post in posts:
        print(post.get("data", {}).get("title"))
