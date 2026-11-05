#!/usr/bin/python3
"""Recursively counts keywords in the hot post titles of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Prints a sorted count of the given keywords found in hot titles."""
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_dev)"}
    params = {"limit": 100, "after": after}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return
    try:
        data = response.json().get("data", {})
    except ValueError:
        return
    words = [w.lower() for w in word_list]
    for post in data.get("children", []):
        title_words = post.get("data", {}).get("title", "").lower().split()
        for word in words:
            counts[word] = counts.get(word, 0) + title_words.count(word)
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    for word, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        if n > 0:
            print("{}: {}".format(word, n))
