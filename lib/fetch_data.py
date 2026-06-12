"""
fetch_data.py
-------------
Step 4: Uses the requests library to fetch data from a public API
and saves results to a structured CSV using pandas.
"""

import requests
import pandas as pd
from datetime import datetime


BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_posts(limit: int = 10) -> list[dict]:
    """Fetch a list of posts from the JSONPlaceholder API."""
    response = requests.get(f"{BASE_URL}/posts", params={"_limit": limit})
    if response.status_code == 200:
        return response.json()
    print(f"  [WARNING] Failed to fetch posts. Status code: {response.status_code}")
    return []


def fetch_single_post(post_id: int = 1) -> dict:
    """Fetch a single post by ID."""
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        return response.json()
    return {}


def save_posts_to_csv(posts: list[dict], filename: str) -> None:
    """Save a list of post dictionaries to a CSV file using pandas."""
    df = pd.DataFrame(posts)
    df.columns = [col.upper() for col in df.columns]   # uppercase column headers
    df.to_csv(filename, index=False)


if __name__ == "__main__":
    print("\n── Fetching single post ──")
    post = fetch_single_post(1)
    print(f"  Title : {post.get('title', 'N/A')}")
    print(f"  Body  : {post.get('body', 'N/A')[:60]}...")

    print("\n── Fetching top 10 posts ──")
    posts = fetch_posts(limit=10)
    print(f"  Retrieved {len(posts)} posts")

    csv_file = f"posts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    save_posts_to_csv(posts, csv_file)
    print(f"  Saved to {csv_file}")