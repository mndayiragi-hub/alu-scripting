#!/usr/bin/python3
"""Queries the Reddit API for the number of subscribers of a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers, or 0 for an invalid subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    try:
        return response.json().get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0
